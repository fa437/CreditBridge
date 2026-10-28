import os

from flask import Flask

from app.extensions import db, migrate, login_manager, csrf


def create_app():
    """Create and configure the CreditBridge Flask application."""

    app = Flask(__name__, instance_relative_config=True)

    # Load the default application configuration.
    app.config.from_object("app.config.Config")

    # Allow local environment variables to override defaults.
    app.config.from_prefixed_env()

    # Ensure the instance directory exists for local application data.
    os.makedirs(app.instance_path, exist_ok=True)

    # Initialise shared extensions.
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Configure login behaviour.
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    # Register application routes.
    from app.routes import register_routes
    register_routes(app)

    return app
