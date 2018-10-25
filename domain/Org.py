from infra.DomainStore import db
from sqlalchemy import Column, Integer, String, DateTime

class Org(db.Model):
  __tablename__ = 'orgs'
  id_org = db.Column(db.Integer, primary_key=True)
  ds_name = db.Column(db.String)

  def to_json(self):
    return {
      'id': self.id_org,
      'nome': self.ds_name,
    }