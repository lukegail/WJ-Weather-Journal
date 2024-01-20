import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# app.debug = True    currently using flask run --debug instead of app.debug = True

# Configure session to use filesystem (instead of signed cookies)
# configures Flask to store sessions on the local filesystem (i.e., disk)
# as opposed to storing them inside of (digitally signed) cookies, which is Flask’s default.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///weather.db")


# disables caching of responses (provided you’re in debugging mode, default in code50 codespace),
# lest you make a change to some file but your browser doesn't notice
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


""" displays user name below the navbar on every page (see layout.html)
Context Processor: Automatically make a dict available in the context of all templates in a Flask app"""
@app.context_processor # displays user name below the navbar on every page
def inject_user_details():
    if "user_id" in session:
        username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]['username']
        return dict(username=username)
    else:
        # Return an empty dictionary or default values when the user is not logged in
        return dict(username=None)


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    if request.method == "POST":

        form_data = {
            'temp': request.form.get("temp"),
            'wind_speed': request.form.get("windSpeed"),
            'wind_direction': request.form.get("windDirection"),
            'air_notes': request.form.get("airNotes"),
            'humidity': request.form.get("humidity"),
            'cloud_coverage': request.form.get("cloudCoverage"),
            'cloud_speed': request.form.get("cloudSpeed"),
            'cloud_altitude': request.form.get("cloudAltitude"),
            'precipitation': request.form.get("precipitation"),
            'water_notes': request.form.get("waterNotes"),
            'moon_phase': request.form.get("moonPhase"),
            'bio_notes': request.form.get("bioNotes")
        }

        valid_directions = {'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N', 'NNE', 'NE', 'ENE'}
        valid_cloud_speeds = {'still', 'slow', 'med', 'fast'}
        valid_cloud_altitudes = {'low', 'med', 'high'}
        valid_precipitations = {'fog', 'rain (barely)', 'rain (light)', 'rain (moderate)', 'rain (heavy)', 'sleet', 'hail', 'snow (light)', 'snow (moderate)', 'snow (heavy)'}
    
        # validate and convert
        for field, value in form_data.items():
            if value:  # Skip validation if field is empty
                try:
                    if field in ['humidity', 'cloud_coverage', 'wind_speed', 'moon_phase']:
                        int_value = int(value)

                        if field in ['humidity', 'cloud_coverage'] and not (0 <= int_value <= 100):
                            return apology(f"{field} must be between 0 and 100", 400)
                        
                        elif field == 'moon_phase' and not (1 <= int_value <= 28):
                            return apology("moon phase must be between 1 and 28", 400)
                        
                        form_data[field] = int_value  # Store the converted integer

                    elif field == 'temp':
                        form_data[field] = round(float(value), 1)  # Round to 1 decimal place and store as float

                except ValueError:
                    return apology(f"Invalid input for {field}", 400)
                
                if field == 'wind_direction' and value not in valid_directions:
                    return apology(f"Invalid input for {field}", 400)
                
                elif field == 'cloud_speed' and value not in valid_cloud_speeds:
                    return apology(f"Invalid input for {field}", 400)
                
                elif field == 'cloud_altitude' and value not in valid_cloud_altitudes:
                    return apology(f"Invalid input for {field}", 400)
                
                elif field == 'precipitation' and value not in valid_precipitations:
                    return apology(f"Invalid input for {field}", 400)
                
        



    
    else:    
        return render_template("index.html")






""" @app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    

    if request.method == "POST":
        # get username and password from registration form
        symbol = request.form.get("symbol").upper()

        # Ensure username was submitted
        if not symbol:
            return apology("must provide symbol", 400)

        # get quote info (dict) for symbol,
        quote_info = lookup(symbol)

        # apology if a lookup error occurs or the symbol is invalid (lookup will return None)
        if not quote_info:
            return apology("stock quote error", 400)

        # formats latest stock price as $usd.00
        price = usd(quote_info["price"])

        return render_template("quoted.html", symbol=symbol, price=price)
    else:
        return render_template("quote.html")"""



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        # uses check_password_hash to compare hashes of users’ passwords
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        # login “remembers” that a user is logged in by storing his or her user_id, an INTEGER, in session.
        # That way, any of this file’s routes can check which user, if any, is logged in.
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        # once the user has successfully logged in, login will redirect to "/",
        # taking the user to their home page.
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


""" allows a user to register for an account via a form.

1. Require that a user input a username, implemented as a text field whose name is username.
    Render an apology if the user’s input is blank or the username already exists.
2. Require that a user input a password, implemented as a text field whose name is password,
    and then that same password again, implemented as a text field whose name is confirmation.
    Render an apology if either input is blank or the passwords do not match.
3. Submit the user’s input via POST to /register.
4. INSERT the new user into users, storing a hash of the user’s password, not the password itself.
    Hash the user’s password with generate_password_hash Odds are you’ll want to create
    a new template (e.g., register.html) that’s quite similar to login.html.

Once you’ve implemented register correctly, you should be able to register for an account
    and log in (since login and logout already work)! And you should be able to see your rows via phpLiteAdmin or sqlite3.
"""
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # get username and password from registration form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure valid password confirmation
        elif confirmation != password:
            return apology("password confirmation failed", 400)

        # Query database for username
        matches = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(matches) != 0:
            return apology("username already exists", 400)

        # hashes (encrypts) the password
        password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

        # inserts the new user's data into the users table in your database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password_hash)

        # Retrieves and sets the session's user ID to the ID of the most recently inserted user in the database
        session["user_id"] = db.execute("SELECT last_insert_rowid()")[0]["last_insert_rowid()"]

        return redirect("/")
    else:
        return render_template("register.html")


