from flask import Flask, render_template
from .view import home, profile

# register all the blueprints for the different views
app = Flask(__name__)
app.register_blueprint(home.routes)
app.register_blueprint(profile.routes)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
