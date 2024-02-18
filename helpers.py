from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400):
    """ Renders an apology to the user (apology text, optional code)
    Returns: (template, code) """
    def escape(s):
        """ Escapes special characters for safe HTML (prevents XSS).
        Returns: escaped string
        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"), ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """ Decorator to enforce user login for protected routes.
    If a user is not logged in (no 'user_id' in session), redirects to the login page.
    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)  # Preserve the original function's metadata
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:  # Check if user is not logged in.
            return redirect("/login")  # Redirect to login page if not logged in.
        return f(*args, **kwargs)  # Call the original function if logged in.
    return decorated_function  # Return the wrapped function.
