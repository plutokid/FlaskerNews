from flask import Blueprint, render_template

routes = Blueprint('about', __name__)

@routes.route("/about")
def about():
    return render_template('about.html')