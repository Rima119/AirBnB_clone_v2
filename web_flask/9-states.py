#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
