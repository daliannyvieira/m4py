from flask_sqlalchemy import SQLAlchemy, Model

class CustomModel(Model):
    def __init__(self, **kwargs):
        for key, value in kwargs:
            setattr(self, key, value)

db = SQLAlchemy(model_class=CustomModel)