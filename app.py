from dotenv import load_dotenv
load_dotenv()  # load environment variables from .env -- this will only happen in development

import os
import pytz

from cs50 import SQL
from datetime import datetime, timedelta
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")  # set secret key for session [set in .env (development) or PythonAnywhere environment variables (production)]
app.config["SESSION_PERMANENT"] = True  # Configure the session to be permanent and set its lifetime
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)  # hardcoding lifetime because i'm trying to keep it simple vs using environment variables, which would require me to delete the hardcoded lifetime for development.

db = SQL("sqlite:///weather.db")  # Configure CS50 Library to use SQLite database


""" Disables caching of responses in the browser while in development.
Ensures the browser always fetches the latest version of files from the server.
Conditionally ensures responses aren't cached in dev/debug mode to accurately reflect code changes. """
@app.after_request
def after_request(response):
    if os.getenv('FLASK_ENV') == 'development':
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"  # no-cache: Prevents caching by the browser or intermediate proxies. // no-store: Prohibits storing the response in any form. // must-revalidate: Forces revalidation with the server on each request.
        response.headers["Expires"] = 0  # Sets an immediate expiration time, indicating the response is stale.
        response.headers["Pragma"] = "no-cache"  # An older header for compatibility with older browsers.
    return response


""" Injects 'username' for dynamic navbar display in layout.html. 
If a user is logged in (identified by 'user_id' in session), it fetches and injects the user's username to personalize the navbar link ('{{ username }}'s history').
If not logged in, 'username' is set to None, affecting no direct change but supporting conditional display logic in layout.html. """
@app.context_processor
def inject_user_details():
    if "user_id" in session:
        username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]['username']
        return dict(username=username)
    else:
        return dict(username=None)


# Receives form data from weather entry page, validates it, and stores it in the database. 
@app.route("/", methods=["GET", "POST"])
@login_required  # only logged-in users can access this route.
def index():
    if request.method == "POST":  # Process form submission
        # Collect form data into a dictionary. Each key corresponds to a form field name.
        form_data = {
            'temp': request.form.get("temp"),
            'wind_speed': request.form.get("windSpeed"),
            'wind_direction': request.form.get("windDirection"),
            'air_notes': request.form.get("airNotes"),
            'humidity': request.form.get("humidity"),
            'cloud_coverage': request.form.get("cloudCoverage"),
            'cloud_speed': request.form.get("cloudSpeed"),
            'cloud_direction': request.form.get("cloudDirection"),
            'cloud_altitude': request.form.get("cloudAltitude"),
            'precipitation': request.form.get("precipitation"),
            'water_notes': request.form.get("waterNotes"),
            'moon_phase': request.form.get("moonPhase"),
            'bio_notes': request.form.get("bioNotes")
        }

        # Define valid values for specific fields
        valid_directions = {'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N', 'NNE', 'NE', 'ENE'}
        valid_cloud_speeds = {'still', 'slow', 'med', 'fast'}
        valid_cloud_altitudes = {'low', 'med', 'high'}
        valid_precipitations = {'fog', 'rain (barely)', 'rain (light)', 'rain (moderate)', 'rain (heavy)', 'sleet', 'hail', 'snow (light)', 'snow (moderate)', 'snow (heavy)'}
    
        # validate and convert
        for field, value in form_data.items():
            if value:  # Skip validation if field is empty
                try:
                    # Convert numeric fields to integers or floats, and validate ranges
                    if field in ['humidity', 'cloud_coverage', 'wind_speed', 'moon_phase']:
                        int_value = int(value)

                        # validate ranges
                        if field in ['humidity', 'cloud_coverage'] and not (0 <= int_value <= 100):
                            return apology(f"{field} must be between 0 and 100", 400)
                        
                        elif field == 'moon_phase' and not (1 <= int_value <= 28):
                            return apology("moon phase must be between 1 and 28", 400)
                        
                        form_data[field] = int_value  # Update the dictionary with the converted value

                    elif field == 'temp':
                        form_data[field] = round(float(value), 1)  # Round to 1 decimal place and store as float

                except ValueError:
                    # Handle invalid input
                    return apology(f"Invalid input for {field}", 400)
                
                # Validate specific fields against sets of valid values
                if field == 'wind_direction' and value not in valid_directions:
                    return apology(f"Invalid input for {field}", 400)
                
                elif field == 'cloud_speed' and value not in valid_cloud_speeds:
                    return apology(f"Invalid input for {field}", 400)
                
                elif field == 'cloud_direction' and value not in valid_directions:
                    return apology(f"Invalid input for {field}", 400)
                
                elif field == 'cloud_altitude' and value not in valid_cloud_altitudes:
                    return apology(f"Invalid input for {field}", 400)
                
                elif field == 'precipitation' and value not in valid_precipitations:
                    return apology(f"Invalid input for {field}", 400)

        # Empty fields: Replace empty strings or "NULL" with None for database insertion        
        for key in form_data:
            if form_data[key] == "" or form_data[key] == "NULL":
                form_data[key] = None

        # insert validated and cleaned data as a new entry into weather table
        db.execute("INSERT INTO weather_entries (user_id, temp, wind_speed, wind_direction, air_notes, humidity, cloud_coverage, cloud_speed, cloud_direction, cloud_altitude, precipitation, water_notes, moon_phase, bio_notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",             
            session["user_id"], form_data['temp'], form_data['wind_speed'], 
            form_data['wind_direction'], form_data['air_notes'], form_data['humidity'], 
            form_data['cloud_coverage'], form_data['cloud_speed'], form_data['cloud_direction'], 
            form_data['cloud_altitude'], form_data['precipitation'], form_data['water_notes'], 
            form_data['moon_phase'], form_data['bio_notes']       
        )
        
        return redirect("/")  # Redirect to the index page after successful submission
    
    else:  # Handle GET request (display the form)    
        return render_template("index.html")


# Retrieves and displays the user's history of weather entries
@app.route("/history", methods=["GET", "POST"])
@login_required  # only logged-in users can access this route.
def history():

    if request.method == "POST":  # redirects back to the history page, perhaps for refreshing   
        return redirect("/history")
    
    else:  # Retrieve weather entries for the logged-in user, ordered by most recent first.
        entries = db.execute("SELECT * FROM weather_entries WHERE user_id = ? ORDER BY log_time DESC", session["user_id"])

        # adjust timestamps to be in EST
        for entry in entries:
            # Parse the 'log_time' string into a datetime object, assuming ISO format, e.g., "2022-01-01T12:00:00"
            log_time_gmt = datetime.fromisoformat(entry["log_time"])
            
            # Set the timezone to GMT
            log_time_gmt = pytz.timezone('GMT').localize(log_time_gmt)

            # Convert to EST
            log_time_est = log_time_gmt.astimezone(pytz.timezone('America/New_York'))
            
            # Format the datetime object back to a string
            entry["log_time"] = log_time_est.strftime('%Y-%m-%d %H:%M:%S')

    # Render the history page template, passing in the user's weather entries with adjusted timestamps.
    return render_template("history.html", entries=entries)


# user login
@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()  # Clear any existing user session for security

    # User reached route via POST (form submission)
    if request.method == "POST":

        # Validate username presence
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Validate password presence
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # # Retrieve user details from database
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Verify username and securely compare passwords using hashed values
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Store logged-in user's ID in session to track login status across the application
        session["user_id"] = rows[0]["id"]

        # Redirect the user to the journal entry (home) page after successful login
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:  # display login form
        return render_template("login.html")


# user logout
@app.route("/logout")
def logout():

    session.clear()  # Clear any existing user session for security

    return redirect("/login")  # Redirect user to login form


# Registers a new user
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # retrieve form data   
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # validate user input
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif confirmation != password:
            return apology("password confirmation failed", 400)

        # Check for existing username
        matches = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(matches) != 0:
            return apology("username already exists", 400)

        # Securely hash the password for storage
        password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

        # insert user data into the users table in the database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password_hash)

        # Log the newly registered user in by setting their user_id in the session.
        session["user_id"] = db.execute("SELECT last_insert_rowid()")[0]["last_insert_rowid()"]

        # Redirect the user to the journal entry (home) page after successful registration
        return redirect("/")
    else:
        # Show the registration form for GET requests.
        return render_template("register.html")
