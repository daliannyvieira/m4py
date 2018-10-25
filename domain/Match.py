from infra.DomainStore import db
from domain.AllOrgs import AllOrgs

class Match():
  @staticmethod
  def read_all_orgs():
    return AllOrgs.read_all_orgs()

  @staticmethod
  def read_one_org(id_org):
    return AllOrgs.read_one_org(id_org)

  @staticmethod
  def create_org(attributes):
    return AllOrgs.create_org(attributes)

  @staticmethod
  def update_org(id_org, attributes):
    return AllOrgs.update_org(id_org, attributes)

  @staticmethod
  def remove_org(id_org):
    return AllOrgs.remove_org(id_org)