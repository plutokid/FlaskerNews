from flask import Blueprint, g, redirect, url_for, session

routes = Blueprint('vote', __name__)

@routes.route('/vote/<int:id>')
def vote(id):
    if session.get('logged_in'):
        g.db.execute('UPDATE links set votes = votes + 1 WHERE id = ?', [id])
        g.db.commit()
    return redirect(url_for('home.home'))