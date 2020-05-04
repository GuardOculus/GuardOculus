from flask_login import login_required
from flask import render_template

from app.map import bp


@bp.route('/map')
def index():
    return render_template('map.html')
