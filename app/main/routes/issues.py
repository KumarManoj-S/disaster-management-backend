from flask_restplus import Namespace, Resource
from flask import request

from app.main.services.issues import IssuesService

api = Namespace('Issues')


@api.route('issues')
class Issues(Resource):
    def post(self):
        issue = request.json
        issue_id = IssuesService.add_new_issue(issue)
        return {'status': 'success', 'insertedId': issue_id}

    def get(self):
        lat = request.args.get('lat')
        long = request.args.get('long')
        radius = request.args.get('radius')
        coordinate = {}
        if lat:
            coordinate['lat'] = lat
        if long:
            coordinate['long'] = long
        if radius:
            coordinate['radius'] = radius

        issues = IssuesService.get_all_issues(coordinate)
        return {'issues': issues}


@api.route('issues/<issue_id>')
class GetIssues(Resource):
    def get(self, issue_id):
        issue = IssuesService.get_issue_by_id(issue_id)
        return issue


@api.route('issues/clustors')
class ClustorsOfIssues(Resource):
    def get(self):
        lat = request.args.get('lat')
        long = request.args.get('long')
        coordinate = {}
        if lat:
            coordinate['lat'] = lat
        if long:
            coordinate['long'] = long

        clustors_of_issues = IssuesService.get_clustors_of_issues(coordinate)
        return {'clustorsOfIssues': clustors_of_issues}

