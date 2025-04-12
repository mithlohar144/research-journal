# Research Journal Platform

A modern web platform for publishing and reviewing academic research papers, built with Django and Bootstrap.

## Table of Contents

1. [Features](#features)
   - [Paper Management](#paper-management)
   - [User System](#user-system)
   - [Review System](#review-system)
   - [Search & Discovery](#search--discovery)
   - [Modern UI/UX](#modern-uiux)

2. [Technology Stack](#technology-stack)

3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup Steps](#setup-steps)
   - [Configuration](#configuration)

4. [Project Structure](#project-structure)
   - [Directory Layout](#project-structure)
   - [Key Components](#project-structure)

5. [Environment Variables](#environment-variables)
   - [Development](#environment-variables)
   - [Production](#environment-variables)

6. [Security Features](#security-features)
   - [SSL/HTTPS](#security-features)
   - [Protection Mechanisms](#security-features)

7. [Contributing](#contributing)
   - [Guidelines](#contributing)
   - [Pull Request Process](#contributing)

8. [License](#license)

## Features

- **Paper Management**
  - Submit research papers with PDF attachments
  - Add abstracts and categorize papers
  - Tag papers for better organization
  - Track paper status (pending, approved, rejected)

- **User System**
  - User registration and authentication
  - Profile management
  - Role-based access control (authors, reviewers, admins)

- **Review System**
  - Peer review functionality
  - Rating and comment system
  - Review status tracking

- **Search & Discovery**
  - Search papers by title, category, or tags
  - Filter papers by category
  - View related papers

- **Modern UI/UX**
  - Responsive Bootstrap design
  - Clean and academic-focused interface
  - Mobile-friendly layout

## Technology Stack

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite (development) / PostgreSQL (production)
- **Forms**: django-crispy-forms with Bootstrap 5
- **Tagging**: django-taggit

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fullstrak-project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 to access the application.

## Project Structure

```
fullstrak-project/
├── accounts/          # User authentication and profiles
├── papers/           # Research paper management
├── reviews/          # Paper review system
├── categories/       # Paper categories
├── contact/         # Contact form functionality
├── static/          # Static files (CSS, JS, images)
├── templates/       # HTML templates
├── media/          # User-uploaded files
└── research_journal/  # Project settings
```

## Environment Variables

For production deployment, set these environment variables:

- `DJANGO_SECRET_KEY`: Your secret key
- `DJANGO_DEBUG`: Set to 'False' in production
- `DATABASE_URL`: Your database URL
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Security Features

- SSL/HTTPS enforcement in production
- Secure cookie settings
- XSS protection
- CSRF protection
- Content security policies
- HSTS enabled

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
