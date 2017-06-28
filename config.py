import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = 'this-really-needs-to-be-changed'
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://boopjvotmbtyvo:cf9ee1ed5f1d3fac96c3739cf1d560a9154065c9402a01e0f926475652327852@ec2-107-20-255-96.compute-1.amazonaws.com:5432/ddemol63mvcqj1"
