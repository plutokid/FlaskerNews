from flask import Blueprint, render_template, g

routes = Blueprint('profile', __name__)

@routes.route('/u/<user>')
def profile(user):
    """
    Show the user profile
    :param user: String user name
    :return: View
    """
    cur = g.db.execute('select name from users where name = ?', [user])
    results = cur.fetchone()
    if results is not None:
        user = results[0]
    else:
        user = 'User not found'
    return render_template('profile.html', user=user)
