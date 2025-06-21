.PHONY: help install run test clean db-init db-reset lint format

# Default target
help:
	@echo "Flask Job Portal - Available Commands:"
	@echo ""
	@echo "  install     - Install dependencies"
	@echo "  run         - Run the development server"
	@echo "  test        - Run tests"
	@echo "  clean       - Clean up temporary files"
	@echo "  db-init     - Initialize database with sample data"
	@echo "  db-reset    - Reset database (delete and recreate)"
	@echo "  lint        - Run code linting"
	@echo "  format      - Format code with black"
	@echo "  deploy      - Prepare for deployment"

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	@echo "✓ Dependencies installed successfully!"

# Run the development server
run:
	@echo "Starting Flask development server..."
	python run.py

# Run tests
test:
	@echo "Running tests..."
	pytest tests/ -v

# Clean up temporary files
clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "✓ Cleanup completed!"

# Initialize database
db-init:
	@echo "Initializing database..."
	python create_db.py

# Reset database
db-reset:
	@echo "Resetting database..."
	rm -f instance/site.db
	python create_db.py

# Run code linting
lint:
	@echo "Running code linting..."
	flake8 app/ tests/ --max-line-length=100 --ignore=E501,W503

# Format code
format:
	@echo "Formatting code..."
	black app/ tests/ --line-length=100

# Prepare for deployment
deploy:
	@echo "Preparing for deployment..."
	pip install -r requirements.txt
	python create_db.py
	@echo "✓ Deployment preparation completed!"

# Development setup
dev-setup: install db-init
	@echo "✓ Development environment setup completed!"
	@echo ""
	@echo "To start the server, run: make run"
	@echo "To run tests, run: make test" 