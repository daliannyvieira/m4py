from application.App import route, session
from domain.Match import Match
from flask_restplus import Resource
from flask import jsonify, request
from flask_cors import cross_origin

@route.route('/org')
class AllOrgsResource(Resource):
  def get(self):
    try:
      orgs = Match.ler_todas_orgs()
      return jsonify(orgs)
    except Exception as exc:
      return exc, 500

@route.route('/org/<int:id_org>')
class OrgResource(Resource):
  def get(self, id_org):
    try:
      org = Match.ler_org(id_org)
      if org:
        return jsonify(org)
      else:
        return 'org nao encontrada', 404
    except Exception as exc:
      return exc, 500