from flask import Blueprint, request, session, redirect, url_for, flash, render_template, g
from flask_bcrypt import generate_password_hash, check_password_hash

routes = Blueprint('auth', __name__)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    """
    Attempt to login the user if this is a POST or show them the login page
    :return: View
    """
    if request.method == 'POST':
        cur = g.db.execute('select id, name, password from users where name = ?', [request.form['name']])
        result = cur.fetchone()
        if result is not None:
            if check_password_hash(result[2], request.form['password']):
                session['logged_in'] = True
                session['user_name'] = result[1]
                return redirect(url_for('home.home'))
            else:
                error = "Password does not match our records"
            return render_template('login.html', error=error)
        else:
            error = "Name not found"
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@routes.route('/logout')
def logout():
    """
    Logout the user
    :return: View
    """
    if session.get('logged_in'):
        session.pop('logged_in', None)
        session.pop('user_name')
        flash("Logged out")
    return redirect(url_for('home.home'))

@routes.route('/register', methods=['POST'])
def register():
    """
    Create a new user. Check if name exists first.
    :return:
    """
    if request.method == 'POST':
        cur = g.db.execute('SELECT name FROM users WHERE name = ?', [request.form['name']])
        if cur.fetchone() is None and request.form['name'] is not None and request.form['password'] is not None:
            cur = g.db.execute('INSERT INTO users (name, password) VALUES (?, ?)',
                               [request.form['name'], generate_password_hash(request.form['password'])])
            g.db.commit()
            result = cur.lastrowid
            if result > 0:
                session['logged_in'] = True
                session['user_name'] = request.form['name']
                return redirect(url_for('home.home'))
            else:
                error = 'Something went wrong'
                return render_template('login.html', error=error)
        else:
            return render_template('login.html', error="That name is taken")
    else:
        return render_template('login.html')