from flask import Blueprint, request, session, redirect, url_for, flash, render_template, g
from flask_bcrypt import generate_password_hash, check_password_hash

routes = Blueprint('auth', __name__)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cur = g.db.execute('select id, name, password from users where name = ?', [request.form['name']])
        result = cur.fetchone()
        if result is not None:
            if check_password_hash(result[2], request.form['password']):
                session['logged_in'] = True
                session['user_name'] = result[1]
                return redirect(url_for('home.home'))
        else:
            error = "Name or password was incorrect"
            return render_template("login.html", error=error)
    else:
        return render_template("login.html")

@routes.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_name')
    flash("Logged out")
    return redirect(url_for('home.home'))

@routes.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        cur = g.db.execute('INSERT INTO users (name, password) VALUES (?, ?)',
                           [request.form['name'], generate_password_hash(request.form['password'])])
        g.db.commit()
        result = cur.lastrowid
        if result > 0:
            session['logged_in'] = True
            session['user_name'] = request.form['name']
            return redirect(url_for('home.home'))
        else:
            error = "Name or password was incorrect"
            return render_template("login.html", error=error)
    else:
        return render_template("login.html")