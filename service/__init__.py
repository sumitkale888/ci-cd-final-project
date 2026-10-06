from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from .models import Account
from .routes import accounts_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        TESTING=False,
        DATABASE_URI="sqlite:///accounts.db",
        TALISMAN_FORCE_HTTPS=False,
        CORS_ALLOWED_ORIGINS=["http://localhost:3000", "http://127.0.0.1:3000"],
    )
    if test_config:
        app.config.update(test_config)

    Talisman(
        app,
        force_https=app.config.get("TALISMAN_FORCE_HTTPS", False),
        content_security_policy={"default-src": "'self'"},
        frame_options="DENY",
        content_type_options="nosniff",
        referrer_policy="strict-origin-when-cross-origin",
    )
    CORS(
        app,
        resources={r"/accounts/*": {"origins": app.config["CORS_ALLOWED_ORIGINS"]}},
    )
    app.register_blueprint(accounts_bp)
    Account.reset()
    return app
