#!/usr/bin/env python3
"""
Flask Job Portal - Main Application Entry Point
"""

import os
import sys
from app import create_app, db

def main():
    """Main function to run the Flask application."""
    # Get configuration from environment variable
    config_name = os.environ.get('FLASK_CONFIG', 'development')
    
    # Create the Flask application
    app = create_app(config_name)
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(
        host=os.environ.get('FLASK_HOST', '127.0.0.1'),
        port=int(os.environ.get('FLASK_PORT', 5000)),
        debug=app.config.get('DEBUG', True)
    )

if __name__ == "__main__":
    main()

