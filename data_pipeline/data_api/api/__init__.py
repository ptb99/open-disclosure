from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from redis import Redis

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)
    from api.routes import data_bp

    app.register_blueprint(data_bp)
    with app.app_context():
        import api.routes  # Import routes

        db.create_all()  # Create sql tables for our data models

        return app
