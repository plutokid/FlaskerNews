from flask import Blueprint, render_template

routes = Blueprint('profile', __name__)

@routes.route('/u/<username>')
def profile(username):
    return username
