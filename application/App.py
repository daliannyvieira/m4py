import os
from infra.DomainStore import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

service = Flask(__name__)

DATABASE_URI = os.environ.get('DATABASE_URI')

# service.config['SQLALCHEMY_ECHO'] = True
service.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
service.config['CORS_HEADERS'] = 'Content-Type'
service.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db.init_app(service)
cors = CORS(service)
route = Api(service)

engine = create_engine(DATABASE_URI, pool_recycle=280)
Session = sessionmaker(bind=engine)
session = Session()