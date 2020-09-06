from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import os
import logging
from flask_seeder import FlaskSeeder


app = Flask(__name__)
db = SQLAlchemy(app)
seeder = FlaskSeeder()
seeder.init_app(app, db)


with open('app/configuration/config.json', 'r') as config:
    json_reader = json.load(config)

    cloud = json_reader['files']
    secret_key = json_reader['sql']['secret_key']
    db_uri = json_reader['sql']['db_uri']

app.config['SECRET_KEY'] = f'{secret_key}'
app.config['SQLALCHEMY_DATABASE_URI'] = f'{db_uri}'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = f'{cloud}'
app.config.from_object(__name__)


from app.handlers import routes, models
