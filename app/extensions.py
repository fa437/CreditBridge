from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Database integration for SQLite through SQLAlchemy.
db = SQLAlchemy()

# Database schema migrations.
migrate = Migrate()

# User login and session management.
login_manager = LoginManager()

# Protection against cross-site request forgery (CSRF).
csrf = CSRFProtect()
