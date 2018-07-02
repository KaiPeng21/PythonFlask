import os

# 
#   Import Flask Secret Key and Database Parameters environment variables
#

# Secret Code for Flask Sessions
flask_secret = os.environ.get('FLASK_SECRET')

# Database Parameters
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')