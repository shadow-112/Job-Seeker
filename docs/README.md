# Flask Job Portal - Documentation

This document provides detailed information about the Flask Job Portal project structure, development guidelines, and deployment instructions.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Development Setup](#development-setup)
4. [API Documentation](#api-documentation)
5. [Database Schema](#database-schema)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Contributing](#contributing)

## Project Overview

The Flask Job Portal is a web application that connects job seekers with employers. It provides a platform for posting job listings, searching for jobs, and managing applications.

### Key Features

- **User Authentication**: Secure login and registration system
- **Job Management**: Create, edit, and delete job listings
- **Job Search**: Advanced search and filtering capabilities
- **Application System**: Apply for jobs and track applications
- **User Profiles**: Manage personal and professional information
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Architecture

### Technology Stack

- **Backend**: Flask 2.3.3, Python 3.11+
- **Database**: SQLite (development), PostgreSQL (production)
- **ORM**: SQLAlchemy 2.0.21
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Frontend**: HTML5, CSS3, JavaScript, Jinja2 Templates
- **Forms**: Flask-WTF, WTForms
- **Testing**: pytest, pytest-flask

### Project Structure

```
flask-job-portal/
├── app/                    # Main application package
│   ├── __init__.py        # Flask app factory
│   ├── models.py          # Database models
│   ├── forms.py           # Form definitions
│   ├── routes.py          # Route handlers
│   ├── static/            # Static files
│   │   ├── css/           # Stylesheets
│   │   ├── js/            # JavaScript files
│   │   ├── images/        # Image assets
│   │   └── uploads/       # User uploads
│   └── templates/         # HTML templates
├── tests/                 # Test suite
├── docs/                  # Documentation
├── instance/              # Instance-specific files
├── config.py              # Configuration settings
├── run.py                 # Application entry point
├── wsgi.py               # WSGI entry point
├── create_db.py          # Database initialization
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
├── Makefile             # Development tasks
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose
└── README.md            # Project README
```

## Development Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-job-portal.git
   cd flask-job-portal
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python create_db.py
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`

### Using Makefile

For easier development, use the provided Makefile:

```bash
# Install dependencies and setup database
make dev-setup

# Run the development server
make run

# Run tests
make test

# Clean up temporary files
make clean
```

## API Documentation

### Authentication Endpoints

#### POST /login
Authenticate a user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "user",
    "email": "user@example.com",
    "user_type": "job_seeker"
  }
}
```

#### POST /register
Register a new user.

**Request Body:**
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "password123",
  "confirm_password": "password123",
  "user_type": "job_seeker",
  "full_name": "New User",
  "phone": "+1234567890"
}
```

### Job Endpoints

#### GET /jobs
Get all jobs with optional search parameters.

**Query Parameters:**
- `search`: Search term for job title or description
- `location`: Filter by location
- `page`: Page number for pagination

#### POST /post_job
Create a new job listing (employers only).

**Request Body:**
```json
{
  "title": "Software Engineer",
  "description": "We are looking for a skilled software engineer...",
  "requirements": "Python, Flask, 3+ years experience",
  "location": "New York, NY",
  "salary": "$80,000 - $120,000",
  "company": "Tech Corp"
}
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    user_type VARCHAR(20) NOT NULL,
    full_name VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Jobs Table
```sql
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    requirements TEXT,
    location VARCHAR(100),
    salary VARCHAR(100),
    company VARCHAR(100),
    employer_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employer_id) REFERENCES users (id)
);
```

### Applications Table
```sql
CREATE TABLE applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    cover_letter TEXT,
    resume_path VARCHAR(255),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES jobs (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_app.py

# Run tests with coverage
pytest --cov=app tests/
```

### Test Structure

- `tests/test_app.py`: Main application tests
- `tests/test_models.py`: Database model tests
- `tests/test_forms.py`: Form validation tests

## Deployment

### Production Deployment

1. **Set environment variables**
   ```bash
   export FLASK_CONFIG=production
   export SECRET_KEY=your-secret-key
   export DATABASE_URL=postgresql://user:pass@localhost/dbname
   ```

2. **Install production dependencies**
   ```bash
   pip install gunicorn
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn --bind 0.0.0.0:5000 wsgi:app
   ```

### Docker Deployment

1. **Build the image**
   ```bash
   docker build -t flask-job-portal .
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

### Deployment Checklist

- [ ] Set production configuration
- [ ] Configure database (PostgreSQL recommended)
- [ ] Set up environment variables
- [ ] Configure web server (Nginx/Apache)
- [ ] Set up SSL certificate
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Test all functionality

## Contributing

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Write comprehensive tests

### Commit Messages

Use conventional commit messages:

```
feat: add user registration functionality
fix: resolve login authentication issue
docs: update API documentation
test: add tests for job search feature
```

## Support

For questions and support:

1. Check the [Issues](https://github.com/yourusername/flask-job-portal/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

---

**Last updated**: December 2024 