from infra.DomainStore import db
from domain.AllOrgs import AllOrgs

class Match():
  @staticmethod
  def ler_todas_orgs():
    return AllOrgs.ler_todas_orgs()

  @staticmethod
  def ler_org(id_org):
    return AllOrgs.ler_org(id_org)