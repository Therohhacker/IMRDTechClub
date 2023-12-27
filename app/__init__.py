from flask import Flask
from app.Admin.views import admin
from app.User.views import user
from app.Main.main import main
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Registering blueprint 
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(user)

    return app