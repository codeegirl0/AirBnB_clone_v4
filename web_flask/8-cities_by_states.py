#!/usr/bin/python3
"""
     Flask web application
"""
from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
         handle teardown
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city_state_list():
    """
         render from storage
    """
    states = storage.all('State').values()
    return render_template("8-cities_by_states.html", states=states)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
