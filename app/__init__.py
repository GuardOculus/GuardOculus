from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    login.login_view = 'auth.login'
    login.login_message = "Авторизутесь чтобы продолжить"

    from app import models
    
    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    from app.stats import bp as stats_bp
    app.register_blueprint(stats_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    from app.map import bp as map_bp
    app.register_blueprint(map_bp)

    return app
