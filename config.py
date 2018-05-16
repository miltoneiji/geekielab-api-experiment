import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

GEEKIE_API_SHARED_SECRET = "jPsedzb7eEaSKh1CP9qEColMF8GWxNowXd49wfinI5MvxaM6md"

GEEKIE_ORGANIZATION_ID = "10000000000004542"

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
SECRET_KEY = 'my precious'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
