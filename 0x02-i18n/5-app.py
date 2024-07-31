#!/usr/bin/env python3
"""
I am a noob
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _

class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Retrieve a user dictionary or None if the ID cannot be found or not provided."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

@app.before_request
def before_request():
    """Executed before all other functions."""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page."""
    user = g.get('user', None)
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def get_index():
    """The home/index page."""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
