def register_routes(app):
    """Register all CreditBridge routes."""

    # Route registration will be added as we implement each feature.
    @app.route("/")
    def home():
        return "CreditBridge is running!"
