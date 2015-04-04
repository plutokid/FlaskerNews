from flask import Blueprint, g, render_template

routes = Blueprint('home', __name__)

@routes.route('/')
def home():
    cur = g.db.execute('SELECT * FROM links ORDER BY votes DESC LIMIT 10')
    results = cur.fetchall()
    return render_template('home.html', results=results)
