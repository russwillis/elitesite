import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = 'this-really-needs-to-be-changed'
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://russw:russw@localhost:5432/elite"
