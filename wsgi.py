#!/usr/bin/env python3
"""
WSGI entry point for Flask Job Portal
Used for production deployment with Gunicorn, uWSGI, etc.
"""

import os
from app import create_app

# Create the Flask application
app = create_app(os.environ.get('FLASK_CONFIG', 'production'))

if __name__ == "__main__":
    app.run() 