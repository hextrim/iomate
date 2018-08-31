# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

PROFILE_PICS_DIR = 'static/img/profile-pics'
UPLOAD_DIR = 'iomate/static/img/profile-pics'
UPLOAD_CONFIG = os.path.join(BASE_DIR, UPLOAD_DIR)

ISO_UPLOAD_DIR = 'uploads/iso'
UPLOAD_DIR_ISO = 'iomate/uploads/iso'
UPLOAD_CONFIG_ISO = os.path.join(BASE_DIR, UPLOAD_DIR_ISO)

MAX_CONTENT_PATH = 1024 * 1024 * 1024 * 1024 * 1024


TEMPLATE_DIR = '/iomate/templates/configuration_templates'
TEMPLATE_DIR_JENKINS = '/jenkins/jobs'
TEMPLATE_CONFIG = os.path.join(BASE_DIR, TEMPLATE_DIR)
TEMPLATE_CONFIG_JENKINS = os.path.join(BASE_DIR, TEMPLATE_DIR_JENKINS)

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'iomate.db')
#DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 4

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Enable Flask-WTF CSRF protection
WTF_CSRF_ENABLED = True

# Secret key for signing cookies
SECRET_KEY = "Or1t3-13t$-i0M4t3"
#SECRET_KEY = os.urandom(24)

# Application settings
APP_NAME = "ioMate"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Flask-Mail settings
MAIL_SERVER = "hextrim.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "admin@hextrim.com"
MAIL_PASSWORD = "***"
#MAIL_DEFAULT_SENDER

# Flask-User settings
#USER_APP_NAME = APP_NAME
#USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
#USER_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
#USER_ENABLE_CONFIRM_EMAIL = True  # Force users to confirm their email
#USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
#USER_ENABLE_EMAIL = True  # Register with Email
#USER_ENABLE_REGISTRATION = True  # Allow new users to register
#USER_ENABLE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
#USER_ENABLE_USERNAME = False  # Register and Login with username
#USER_AFTER_LOGIN_ENDPOINT = 'user_page'
#USER_AFTER_LOGOUT_ENDPOINT = 'home_page'

# Flask-Security
# https://pythonhosted.org/Flask-Security/configuration.html
SECURITY_PASSOWRD_HASH = 'bcrypt'
#SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = SECRET_KEY
SECURITY_FLASH_MESSAGES = True
SECURITY_TRACKABLE = True
SECURITY_REGISTERABLE = True
SECURITY_EMAIL_SENDER = "admin@hextrim.com"
#SECURITY_REGISTER_URL 
SECURITY_RECOVERABLE = True
#SECURITY_RESET_URL 
#SECURITY_CONFIRMABLE = True
#SECURITY_CONFIRM_URL
SECURITY_TOKEN_MAX_AGE = 28800
#SECURITY_UNAUTHORIZED_VIEW

# Flask-Security + Flask-Admin
#SECURITY_POST_LOGIN_VIEW = "/admin/"
#SECURITY_POST_LOGOUT_VIEW = "/admin/"
#SECURITY_POST_REGISTER_VIEW = "/admin/"

