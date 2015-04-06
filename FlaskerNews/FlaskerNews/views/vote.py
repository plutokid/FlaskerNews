from flask import Blueprint, g, redirect, url_for, session

routes = Blueprint('vote', __name__)

@routes.route('/vote/<int:link_id>')
def vote(link_id):
    """
    Increment the links votes by one
    :param link_id: int Id of the link
    :return: View
    """
    if session.get('logged_in'):
        g.db.execute('UPDATE links set votes = votes + 1 WHERE id = ?', [link_id])
        g.db.commit()
    return redirect(url_for('home.home'))