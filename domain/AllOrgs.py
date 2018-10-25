from infra.DomainStore import db
from domain.Org import Org

class AllOrgs():
  @staticmethod
  def ler_todas_orgs():
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
  def ler_org(id_org):
    try:
      org = db.session.query(Org).filter_by(id_org = id_org).first()
      return org.to_json() if org else None
    except:
      db.session.rollback()
      raise