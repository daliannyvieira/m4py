from infra.DomainStore import db
from domain.Org import Org

class AllOrgs():
  @staticmethod
  def read_all_orgs():
    try:
      orgs = db.session.query(Org).all()
      orgs_lista = []
      for org in orgs:
        orgs_lista.append(org.to_json())
      return orgs_lista
    except:
      db.session.rollback()
      raise

  @staticmethod
  def create_org(attributes):
    try:
      new_org = Org()
      new_org.ds_name = attributes['ds_name']
      db.session.add(new_org)
      db.session.commit()
      return new_org.to_json()
    except Exception as e:
      db.session.rollback()
      raise

  @staticmethod
  def read_one_org(id_org):
    try:
      org = db.session.query(Org).filter_by(id_org = id_org).first()
      return org.to_json() if org else None
    except:
      db.session.rollback()
      raise

  @staticmethod
  def update_org(id_org, attributes):
    try:
      db.session.query(Org)\
        .filter_by(id_org = id_org)\
        .update(attributes)
      db.session.commit()
    except:
      db.session.rollback()
      raise

  @staticmethod
  def remove_org(id_org):
    try:
      org = db.session.query(Org)\
        .filter_by(id_org = id_org)\
        .first()
      if not org:
        return None
      db.session.delete(org)
      db.session.commit()
      return { 'message': 'org was removed' }
    except:
      db.session.rollback()
      raise