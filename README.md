# WJ Weather Journal

## CS50 Final Project
####
This project was developed as my final project for Harvard University's CS50x, an introduction to computer science.

#### Video Demo:  https://youtu.be/tK0F-RNwDUg

## Overview
####
WJ Weather Journal is a Flask-based web app for weather enthusiasts, researchers, or anyone interested in documenting real-time weather observations and tracking weather patterns over time. WJ features user authentication, dynamic content rendering, and a detailed form for data entry, making it accessible and intuitive on both mobile and desktop devices, although its main use case is for mobile devices. Welcome to your personal weather journal!

## Features
####
• **User Authentication:** Secure login and registration to manage user access.

• **Long Session Lifetime:** Set to 30 days to facilitate frequent, spontaneous use without the need for constant logins.

• **Weather Logging:** Users can log various weather conditions into fields loosely organized into sections related to air (temperature, wind), water (humidity, clouds, precipitation), and extras (moon, bio [flora and fauna]), encouraging users to think about weather in a structured, comprehensive way. There are no mandatory fields, allowing flexibility of data entry.

• **Automatic Timestamps:** The app automatically timestamps each entry, adjusting for EST and accounting for daylight savings, to create an accurate timeline of observations.

• **Historical Data Viewing:** Users can view their history of weather entries, so they can track changes over time and recall specific logged observations.

• **Data Validation:** Ensures the accuracy and integrity of the weather data recorded through backend validation (in both python and the SQLite database).

• **Responsive Web Design:** The app includes dynamic form elements such as sliders and dropdowns for an engaging user experience. Toggle switches enable users to show or hide detailed input sections, reducing clutter and focusing the user's attention. These elements work well on both mobile and desktop devices (tested only on iOS (for mobile) and Firefox and Chrome (for desktop)).

• **Easy-to-use Slider Thumbs:** Sliders are designed with large "thumbs" for ease of use, especially on mobile devices.

• **Custom Weather Notes:** Allows users to add personalized notes to their weather entries for recording additional observations.

• **Image Support for Moon Phases:** Dynamically displays images representing the phase of the moon.

• **High Contrast Dark Mode & Streamlined Design:** High contrast dark mode to conserve battery on mobile devices and enhance visibility in various lighting conditions. Design is streamlined and minimalistic, prioritizing speed and efficiency for frequent, practical use. Avoids unnecessary features and heavy imagery, ensuring optimal performance even in areas with poor data reception, while conserving battery life.

## Technical Stack
####
• **Frontend:** HTML, CSS (with Bootstrap), JavaScript.

• **Backend:** Python with Flask and Jinja for server-side logic and routing.

• **Database:** SQLite for storing user data and weather entries, accessed via CS50 Library.

• **Security:** Werkzeug for password hashing and Flask session management for user authentication.

## Application Structure
####
• **app.py:** Main application file for route definitions and Flask app is configuration.

• **helpers.py:** Contains functions: apology error rendering and login_required decorators.

• **templates/:** HTML template directory, utilizing Jinja2. Includes layout.html for the base template, index.html for the weather entry form, and history.html for the display of previous entries.

• **static/:** Contains CSS and JavaScript files, a directory of moon phase images, and a favicon.

## Running the App
####
• Use *'flask run'* to start a local development server that hosts the Flask app. (I use *'flask run --host=0.0.0.0 --debug --port=5001'*, making it accessible over my local network on port 5001, with debug features enabled.)

## Usage
####
• **Register/Login:** Users can create an account or log in to access weather journaling features. Use the hyperlinks in the navbar. On mobile devices, these options are available in the navbar's hamburger menu.

• **Record Weather Conditions:** Using the form on the index page, users submit weather observations. Logged-in users can return to this page any time by clicking "WJ" on the left side of the navbar.

• **View History:** Users can see all of their own previous weather entries, starting with the most recent, and continuing in reverse chronological order. Access history using the hyperlink in the navbar. On mobile devices, this option is found in the navbar's hamburger menu.

## Upcoming Features
####
• **Edit/Delete Entries:** Users will be able to modify or remove their weather entries, in whole or any individual fields.

• **Time Zone Adjustments:** Users will have the option to specify their time zone for entries.

• **Unit Adjustments:** User will be able to toggle F/C and mph/kph.

• **Dynamic Moon Phases:** The app will generate images representing the moon's phase using a trigonometric function to represent the curvature of the shadow/illumination line, instead of relying on a directory of static images (the current strategy).