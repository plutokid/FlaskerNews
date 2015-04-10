from flask import Blueprint, g, render_template, request

routes = Blueprint('search', __name__)

@routes.route('/search')
def search():
    if request.args.get('query') is not None:
        cur = g.db.execute("SELECT * FROM links WHERE title LIKE ?", ['%' + request.args.get('query') + '%'])
        results = cur.fetchall()
        return render_template('search.html', results=results)
    else:
        return render_template('search.html', results=None)