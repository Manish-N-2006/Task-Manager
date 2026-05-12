from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.models import tasks
    from app.routes import register_routes
    register_routes(app)

    @app.route("/")
    def home():
        return {
            "msg" : "Task Manager API running !!"
        }
    return app