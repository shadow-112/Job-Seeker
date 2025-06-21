# 🚀 Flask Job Portal

A modern, feature-rich job portal web application built with Flask, Python, and SQLAlchemy. This application allows job seekers to search and apply for jobs, while employers can post job listings and manage applications.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.21-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### For Job Seekers
- 🔍 **Advanced Job Search** - Search jobs by title, location, and keywords
- 📝 **Resume Upload** - Upload and manage your resume/CV
- 📋 **Application Tracking** - Track your job applications
- 👤 **User Profile** - Create and manage your profile
- 🔔 **Application Notifications** - Get notified about application status

### For Employers
- 📊 **Job Posting** - Create and manage job listings
- 👥 **Application Management** - Review and manage job applications
- 📈 **Dashboard** - Overview of posted jobs and applications
- 🔍 **Candidate Search** - Search through applicant profiles

### General Features
- 🔐 **User Authentication** - Secure login and registration system
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🎨 **Modern UI** - Clean and intuitive user interface
- 🔒 **Security** - Password hashing and CSRF protection
- 📊 **Database** - SQLite database with SQLAlchemy ORM

## 🛠️ Technology Stack

- **Backend**: Python 3.11+, Flask 2.3.3
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript, Jinja2 Templates
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Forms**: Flask-WTF, WTForms
- **Styling**: Custom CSS with responsive design

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.11 or higher
- pip (Python package installer)
- Git

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shadow-112/flask-job-portal.git
cd flask-job-portal
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database

```bash
python create_db.py
```

### 5. Run the Application

```bash
python run.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
flask-job-portal/
├── app/                    # Main application package
│   ├── __init__.py        # Flask app initialization
│   ├── models.py          # Database models
│   ├── forms.py           # Form definitions
│   ├── routes.py          # Route handlers
│   ├── static/            # Static files (CSS, JS, images)
│   │   ├── css/           # Stylesheets
│   │   ├── js/            # JavaScript files
│   │   ├── images/        # Image assets
│   │   └── uploads/       # User uploads
│   └── templates/         # HTML templates
│       ├── layout.html    # Base template
│       ├── login.html     # Login page
│       ├── register.html  # Registration page
│       ├── show_jobs.html # Job listings
│       └── ...            # Other templates
├── instance/              # Instance-specific files
│   └── site.db           # SQLite database
├── tests/                 # Test suite
├── docs/                  # Documentation
├── requirements.txt      # Python dependencies
├── run.py               # Application entry point
├── create_db.py         # Database initialization
└── README.md            # This file
```

## 🔧 Configuration

The application uses the following configuration:

- **Secret Key**: Configured in `config.py`
- **Database**: SQLite database stored in `instance/site.db`
- **Debug Mode**: Enabled for development

To customize the configuration, modify the settings in `config.py`.

## 📖 Usage

### For Job Seekers

1. **Register/Login**: Create an account or log in to your existing account
2. **Browse Jobs**: Use the search functionality to find relevant jobs
3. **Upload Resume**: Upload your resume/CV in the profile section
4. **Apply for Jobs**: Click "Apply" on job listings you're interested in
5. **Track Applications**: Monitor your application status in the dashboard

### For Employers

1. **Register/Login**: Create an employer account or log in
2. **Post Jobs**: Create new job listings with detailed descriptions
3. **Review Applications**: View and manage incoming applications
4. **Contact Candidates**: Reach out to promising candidates

## 🧪 Testing

To run tests for the application:

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_app.py
```

## 🛠️ Development

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

## 🐳 Docker

### Quick Start with Docker

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t flask-job-portal .
docker run -p 5000:5000 flask-job-portal
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- SQLAlchemy for the powerful ORM
- All contributors who have helped improve this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/shadow-112/flask-job-portal/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 📚 Documentation

For detailed documentation, API reference, and development guidelines, see the [docs/README.md](docs/README.md) file.

---

**Made with ❤️ using Flask and Python**
