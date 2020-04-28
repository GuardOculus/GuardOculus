from flask import render_template

from app.stats import bp


@bp.route('/')
@bp.route('/stats')
def index():
    return render_template('stats.html')
