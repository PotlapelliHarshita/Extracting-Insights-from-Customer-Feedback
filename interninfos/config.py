import os
from dotenv import load_dotenv

load_dotenv()

_INVALID_SECRET_VALUES = {
    "",
    "dev-jwt-secret-key-12345",
    "dev-secret",
    "replace-with-a-secure-secret",
    "replace-with-a-flask-secret",
}


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', '').strip() or None
    REDIS_URL = os.getenv('REDIS_URL', '').strip() or None
    SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL', '').strip() or None
    SMTP_HOST = os.getenv('SMTP_HOST', '').strip() or None
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', '').strip() or None
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '').strip() or None
    SMTP_FROM_EMAIL = os.getenv('SMTP_FROM_EMAIL', '').strip() or None
    ALERT_EMAIL_TO = os.getenv('ALERT_EMAIL_TO', '').strip() or None

    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', '5432'))
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'postgres')
    DB_SSLMODE = os.getenv('DB_SSLMODE', 'require')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '').strip() or None
    FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', '').strip() or None
    MIN_PASSWORD_LENGTH = int(os.getenv('MIN_PASSWORD_LENGTH', '8'))

    @classmethod
    def validate_runtime_secrets(cls):
        invalid = [
            name for name, value in {
                "JWT_SECRET_KEY": cls.JWT_SECRET_KEY or "",
                "FLASK_SECRET_KEY": cls.FLASK_SECRET_KEY or "",
            }.items()
            if value in _INVALID_SECRET_VALUES
        ]
        if invalid:
            raise RuntimeError(f"Set secure values for: {', '.join(invalid)}")
