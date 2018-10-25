from application.App import route, session
from domain.Match import Match
from flask_restplus import Resource
from flask import jsonify, request
from flask_cors import cross_origin

@route.route('/org')
class AllOrgsResource(Resource):
  def get(self):
    try:
      orgs = Match.read_all_orgs()
      return jsonify(orgs)
    except Exception as exc:
      return exc, 500

  def post(self):
    try:
      json = request.get_json()
      org = Match.create_org(json)
      org = jsonify(org)
      org.status_code = 201
      return org
    except Exception as exc:
      return exc, 500

@route.route('/org/<int:id_org>')
class OrgResource(Resource):
  def get(self, id_org):
    try:
      org = Match.read_one_org(id_org)
      if org:
        return jsonify(org)
      else:
        return 'org nao encontrada', 404
    except Exception as exc:
      return exc, 500

  def put(self, id_org):
    try:
      attributes = request.get_json()
      Match.update_org(id_org, attributes)
      return "organization updated.", 200
    except Exception as exc:
      return exc, 500

  def delete(self, id_org):
    try:
      org = Match.remove_org(id_org)
      if org:
        return jsonify(org)
      else:
        return 'ORG_NOT_FOUND', 404
    except Exception as exc:
      return exc, 500
