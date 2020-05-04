from flask import render_template
from flask_login import login_required

from app.stats import bp


@bp.route('/')
@bp.route('/stats')
@login_required
def index():
    return render_template('stats.html')
