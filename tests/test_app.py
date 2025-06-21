"""
Test cases for Flask Job Portal application
"""

import pytest
import os
import tempfile
from app import create_app, db
from app.models import User, Job, Application
from flask_bcrypt import Bcrypt

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app('testing')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    
    # Create the database and load test data
    with app.app_context():
        db.create_all()
        
        # Create test users
        bcrypt = Bcrypt(app)
        
        # Test job seeker
        job_seeker = User(
            username='test_seeker',
            email='test_seeker@example.com',
            password_hash=bcrypt.generate_password_hash('testpass').decode('utf-8'),
            user_type='job_seeker',
            full_name='Test Seeker',
            phone='+1234567890'
        )
        
        # Test employer
        employer = User(
            username='test_employer',
            email='test_employer@example.com',
            password_hash=bcrypt.generate_password_hash('testpass').decode('utf-8'),
            user_type='employer',
            full_name='Test Employer',
            phone='+0987654321'
        )
        
        db.session.add(job_seeker)
        db.session.add(employer)
        db.session.commit()
        
        # Create test job
        test_job = Job(
            title='Test Job',
            description='This is a test job description',
            requirements='Test requirements',
            location='Test Location',
            salary='$50,000 - $70,000',
            company='Test Company',
            employer_id=employer.id
        )
        
        db.session.add(test_job)
        db.session.commit()
    
    yield app
    
    # Clean up the temporary database
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

class TestApp:
    """Test cases for the Flask application."""
    
    def test_home_page(self, client):
        """Test that the home page loads successfully."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Job Portal' in response.data
    
    def test_register_page(self, client):
        """Test that the registration page loads successfully."""
        response = client.get('/register')
        assert response.status_code == 200
        assert b'Register' in response.data
    
    def test_login_page(self, client):
        """Test that the login page loads successfully."""
        response = client.get('/login')
        assert response.status_code == 200
        assert b'Login' in response.data
    
    def test_jobs_page(self, client):
        """Test that the jobs page loads successfully."""
        response = client.get('/jobs')
        assert response.status_code == 200
        assert b'Jobs' in response.data
    
    def test_user_registration(self, client):
        """Test user registration functionality."""
        response = client.post('/register', data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'confirm_password': 'newpass123',
            'user_type': 'job_seeker',
            'full_name': 'New User',
            'phone': '+1111111111'
        }, follow_redirects=True)
        
        assert response.status_code == 200
    
    def test_user_login(self, client):
        """Test user login functionality."""
        response = client.post('/login', data={
            'email': 'test_seeker@example.com',
            'password': 'testpass'
        }, follow_redirects=True)
        
        assert response.status_code == 200
    
    def test_job_creation(self, client):
        """Test job creation functionality."""
        # First login as employer
        client.post('/login', data={
            'email': 'test_employer@example.com',
            'password': 'testpass'
        })
        
        # Create a new job
        response = client.post('/post_job', data={
            'title': 'New Test Job',
            'description': 'New test job description',
            'requirements': 'New test requirements',
            'location': 'New Test Location',
            'salary': '$60,000 - $80,000',
            'company': 'New Test Company'
        }, follow_redirects=True)
        
        assert response.status_code == 200
    
    def test_job_search(self, client):
        """Test job search functionality."""
        response = client.get('/jobs?search=Test')
        assert response.status_code == 200
        assert b'Test Job' in response.data
    
    def test_404_error(self, client):
        """Test 404 error handling."""
        response = client.get('/nonexistent')
        assert response.status_code == 404

class TestModels:
    """Test cases for database models."""
    
    def test_user_model(self, app):
        """Test User model functionality."""
        with app.app_context():
            user = User.query.filter_by(username='test_seeker').first()
            assert user is not None
            assert user.email == 'test_seeker@example.com'
            assert user.user_type == 'job_seeker'
    
    def test_job_model(self, app):
        """Test Job model functionality."""
        with app.app_context():
            job = Job.query.filter_by(title='Test Job').first()
            assert job is not None
            assert job.company == 'Test Company'
            assert job.location == 'Test Location'
    
    def test_application_model(self, app):
        """Test Application model functionality."""
        with app.app_context():
            # Create a test application
            job = Job.query.first()
            user = User.query.filter_by(user_type='job_seeker').first()
            
            application = Application(
                job_id=job.id,
                user_id=user.id,
                cover_letter='Test cover letter',
                resume_path='test_resume.pdf'
            )
            
            db.session.add(application)
            db.session.commit()
            
            # Verify the application was created
            saved_app = Application.query.filter_by(job_id=job.id, user_id=user.id).first()
            assert saved_app is not None
            assert saved_app.cover_letter == 'Test cover letter' 