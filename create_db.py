#!/usr/bin/env python3
"""
Database initialization script for Flask Job Portal
"""

import os
import sys
from app import create_app, db
from app.models import User, Job, Application

def init_db():
    """Initialize the database with tables and sample data."""
    # Create the Flask application
    app = create_app()
    
    with app.app_context():
        # Create all tables
        print("Creating database tables...")
        db.create_all()
        print("✓ Database tables created successfully!")
        
        # Check if we already have data
        if User.query.first():
            print("✓ Database already contains data. Skipping sample data creation.")
            return
        
        # Create sample data
        print("Creating sample data...")
        
        # Create sample users
        from flask_bcrypt import Bcrypt
        bcrypt = Bcrypt(app)
        
        # Sample job seeker
        job_seeker = User(
            username='jobseeker',
            email='jobseeker@example.com',
            password_hash=bcrypt.generate_password_hash('password123').decode('utf-8'),
            user_type='job_seeker',
            full_name='John Doe',
            phone='+1234567890'
        )
        
        # Sample employer
        employer = User(
            username='employer',
            email='employer@example.com',
            password_hash=bcrypt.generate_password_hash('password123').decode('utf-8'),
            user_type='employer',
            full_name='Jane Smith',
            phone='+0987654321'
        )
        
        db.session.add(job_seeker)
        db.session.add(employer)
        db.session.commit()
        
        # Create sample jobs
        sample_jobs = [
            Job(
                title='Python Developer',
                description='We are looking for an experienced Python developer...',
                requirements='Python, Flask, SQLAlchemy, 3+ years experience',
                location='New York, NY',
                salary='$80,000 - $120,000',
                company='Tech Corp',
                employer_id=employer.id
            ),
            Job(
                title='Frontend Developer',
                description='Join our team as a frontend developer...',
                requirements='JavaScript, React, HTML, CSS, 2+ years experience',
                location='San Francisco, CA',
                salary='$70,000 - $110,000',
                company='Web Solutions',
                employer_id=employer.id
            ),
            Job(
                title='Data Scientist',
                description='Exciting opportunity for a data scientist...',
                requirements='Python, Machine Learning, Statistics, PhD preferred',
                location='Boston, MA',
                salary='$90,000 - $140,000',
                company='Data Analytics Inc',
                employer_id=employer.id
            )
        ]
        
        for job in sample_jobs:
            db.session.add(job)
        
        db.session.commit()
        
        print("✓ Sample data created successfully!")
        print("\nSample accounts created:")
        print("Job Seeker: jobseeker@example.com / password123")
        print("Employer: employer@example.com / password123")

if __name__ == "__main__":
    try:
        init_db()
        print("\n🎉 Database initialization completed successfully!")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        sys.exit(1) 