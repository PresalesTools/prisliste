from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from .models import db
from app.routes.upload import upload_bp
from app.routes.cart import cart_bp
from app.routes.product_selection import product_selection_bp
from app.database import db as database
import sys
import os

# Get the parent directory of the current file
current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)

# Add the parent directory to the system path
sys.path.append(parent_directory)

load_dotenv() # Load env var from .env

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'your_secret_key'

# Initialize the database and migration engine
db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(upload_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(product_selection_bp)

if __name__ == '__main__':
    app.run(debug=True)
