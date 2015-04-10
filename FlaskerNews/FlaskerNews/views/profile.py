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
    cur = g.db.execute('SELECT * FROM links WHERE user_name = ? ORDER BY votes DESC', [user])
    results = cur.fetchall()
    links = None
    if results is not None:
        links = results
    else:
        links = 'User has no posts'
    return render_template('profile.html', user=user, links=links)
