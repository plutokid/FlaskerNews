import sqlite3
import os
from flask import Flask, render_template, g, current_app
from .views import home, profile, auth, submit

app = Flask(__name__)

DEBUG = True
SECRET_KEY = "sfdha8e7qwoy86&^FG76OUYBXyuo&^Q67OAOD(P*W*R(#WRF"
DATABASE = os.path.join(app.root_path, 'data/flasker.db')
# register all the blueprints for the different views

app.config.from_object(__name__)
app.register_blueprint(home.routes)
app.register_blueprint(auth.routes)
app.register_blueprint(submit.routes)
app.register_blueprint(profile.routes)


def get_db():
    if not hasattr(g, 'db'):
        g.db = sqlite3.connect(DATABASE)
    return g.db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = get_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
