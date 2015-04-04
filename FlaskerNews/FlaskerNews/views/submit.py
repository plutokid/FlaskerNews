from flask import Blueprint, request, g, redirect, url_for, session, render_template, flash
import time

routes = Blueprint('submit', __name__)


@routes.route('/submit', methods=['GET', 'POST'])
def submit():
    if session.get('logged_in'):
        if request.method == 'GET':
            return render_template('submit.html')
        else:
            if request.form['title'] is not None and request.form['url'] is not None:
                cur = g.db.execute("INSERT INTO links (user_id, title, url, votes, submit_date) VALUES (? , ?, ?, ?, ?)",
                                   [session['user_id'], request.form['title'], request.form['url'], 1,
                                    time.strftime("%d/%m/%Y %H:%M")])
                g.db.commit()
                return str(cur.lastrowid)
    else:
        flash('You must be logged in to submit a new link.')
        return redirect(url_for('auth.login'))