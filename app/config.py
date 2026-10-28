import os


class Config:
    """Configuration settings for CreditBridge."""

    # Keep secret keys outside the source code.
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "dev-only-change-this-before-deployment"
    )

    # Store the SQLite database in the instance directory.
    SQLALCHEMY_DATABASE_URI = "sqlite:///creditbridge.db"

    # Disable unnecessary SQLAlchemy event notifications.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
