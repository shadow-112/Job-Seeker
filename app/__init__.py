from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)
    
    # Import configuration
    from config import config
    app.config.from_object(config[config_name])
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Ensure upload folder exists
    try:
        os.makedirs(app.config['UPLOAD_FOLDER'])
    except OSError:
        pass
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    
    # Configure login manager
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'
    
    # Register blueprints (if any)
    # from app.auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)
    
    # Import routes
    from app import routes
    
    return app

# Create the app instance
app = create_app()

# Import routes after app creation to avoid circular imports
from app import routes
