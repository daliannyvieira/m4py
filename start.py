import os
from application.App import service
from application.OrgService import AllOrgsResource, OrgResource

if __name__ == '__main__':
    DEBUG = True
    CORS_HEADERS = 'Content-Type'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    ENVIRONMENT = os.environ.get('APPLICATION_ENVIRONMENT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    service.debug = True
    service.run(host='0.0.0.0', port=5000, use_reloader=True)