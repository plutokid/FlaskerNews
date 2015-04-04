from flask import Blueprint, request, session, redirect, url_for, flash, render_template, g

routes = Blueprint('auth', __name__)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cur = g.db.execute('select id, name, password from users where name = ? and password = ?',
                           [request.form['name'], request.form['password']])
        result = cur.fetchone()
        if result is not None:
            session['logged_in'] = True
            session['user_id'] = result[0]
            session['name'] = result[1]
            return redirect(url_for('home.home'))
        else:
            error = "Name or password was incorrect"
            return render_template("login.html", error=error)
    else:
        return render_template("login.html")

@routes.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Logged out")
    return redirect(url_for('home.home'))