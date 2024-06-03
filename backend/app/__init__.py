from flask import Flask
from flask_cors import CORS
import pymysql

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'charu2001'
app.config['MYSQL_DB'] = 'materials_objects_db'
app.config['MYSQL_PORT'] = 8889

# Initialize PyMySQL
def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        port=app.config['MYSQL_PORT']
    )

from app import routes
