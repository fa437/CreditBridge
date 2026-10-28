# CreditBridge

CreditBridge is a web application designed to digitise the credit-recognition process for credits earned at another university or within the same university.

The project replaces paper forms, manual signatures, and repeated email communication with a centralised digital workflow.

## Project Status

!!!!!!!Under development.!!!!!

## 1. Problem Statement

The traditional credit-recognition process can rely on paper forms, signatures, and email communication. This can make applications difficult to track and decisions difficult to manage efficiently.

## 2. Proposed Solution

CreditBridge provides a digital platform through which students can submit credit-recognition applications, lecturers can review them, and the Study Centre can finalise the recognition process.

### Application Workflow

1. **Student:** Completes and submits a credit-recognition application with supporting documents.
2. **Lecturer:** Reviews the application and approves or rejects it.
3. **Notification:** If the lecturer rejects the application, the student is notified.
4. **Study Centre:** Finalises the recognition process after the required approval.
5. **Student:** Tracks the application's progress and status.

## 3. User Roles

### Student
- Submit credit-recognition applications.
- Upload supporting documents.
- View application details.
- Track application status.
- Receive notifications about decisions.

### Lecturer
- View assigned applications.
- Review submitted information and documents.
- Approve or reject applications.
- Record decisions and comments.

### Study Centre
- Review applications that have received the required approval.
- Finalise the recognition process.
- Update the final application status.

Access to features and records will be restricted according to each user's role.

## 4. Technology Stack

- **HTML:** Page structure.
- **CSS:** Styling and layout.
- **JavaScript:** Frontend interactions.
- **Python:** Backend programming.
- **Flask:** Web application framework.
- **SQLite:** Relational database.
- **Flask-SQLAlchemy:** Database integration and ORM.
- **pytest:** Automated testing.

## 5. Project Structure

```text
CreditBridge/
├── app.py
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   ├── static/
│   └── utils/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. Prerequisites

- Python 3
- Git
- A web browser
- A terminal

## 7. Installation and Setup

### Step 1: Open the project directory

```bash
cd /home/francis/Documents/CreditBridge
```

### Step 2: Create a virtual environment

```bash
python3 -m venv .venv
```

### Step 3: Activate the virtual environment

On Linux:

```bash
source .venv/bin/activate
```

### Step 4: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Configure the application

Configure the Flask application, database, and required environment variables before running the application.

Do not commit real passwords, secret keys, or other sensitive configuration values to Git.

### Step 6: Start the application

Once the Flask startup code is configured:

```bash
python app.py
```

Open the local URL printed in the terminal.

## 8. Database

CreditBridge uses SQLite as its database.

The database will store information such as:
- User accounts and roles.
- Credit-recognition applications.
- Supporting document metadata.
- Lecturer decisions.
- Application status history.
- Notifications.

The database schema will be managed through SQLAlchemy models and migrations as the project develops.

Local database files must not be committed to Git.

## 9. Testing

Run the automated tests from the project root:

```bash
pytest
```

Tests cover authentication, applications, lecturer decisions, Study Centre processing, and role-based permissions as those features are implemented.

## 10. Development Guidelines

- Keep routes, business logic, database models, and templates separated.
- Validate input on the backend.
- Enforce role-based permissions on the server.
- Protect student records and uploaded documents.
- Use Git for version control.
- Test important workflows before merging changes.
- Never commit credentials or sensitive student information.

## 11. Team Collaboration

The project is developed collaboratively using Git.

The frontend and backend should follow agreed interfaces, form fields, routes, and data structures. Commit focused changes and synchronise with the shared repository carefully to avoid overwriting another team member's work.

## 12. Planned Features

- User authentication.
- Student dashboard and application submission.
- Supporting document uploads.
- Lecturer review and decision recording.
- Study Centre finalisation.
- Application tracking.
- Email notifications.
- Role-based access control.
- Automated tests.
