# WorkFlowHub — Employee & Task Management System

A professional Django portfolio project for internships.

## Features
- Authentication: login/logout/signup
- Role-based dashboard
- Employee CRUD
- Department CRUD
- Project CRUD
- Task CRUD
- Attendance CRUD
- Leave request CRUD
- Search/filtering
- Dashboard statistics
- Django Admin
- REST API for employees, projects and tasks
- Responsive Bootstrap 5 UI

## Setup

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

The project uses SQLite by default so it runs immediately. PostgreSQL can be configured later in settings.py.
