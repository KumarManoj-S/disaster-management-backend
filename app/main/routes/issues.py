from flask_restplus import Namespace, Resource
from flask import request

from app.main.services.issues import IssuesService
from app.main.services.issues_acknowledgement import IssuesAcknowledgementsService
from app.main.services.issues_plus_one import IssuesPlusOnesService

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


@api.route('issues/<issue_id>/acknowledge')
class AcknowledgeIssue(Resource):
    def post(self, issue_id):
        volunteer = request.json
        phone_no = volunteer.get('phoneNo')
        volunteer_id = volunteer.get('volunteerId')
        acknowledgement_id = IssuesAcknowledgementsService.acknowledge(volunteer_id=volunteer_id, phone_no=phone_no,
                                                                       issue_id=issue_id)
        return {'status': 'success', 'insertedId': acknowledgement_id}


@api.route('issues/<issue_id>/plus-one')
class PlusOneIssue(Resource):
    def post(self, issue_id):
        victim = request.json or {}
        phone_no = victim.get('phoneNo')
        volunteer_id = victim.get('victimId')
        name = victim.get('name')
        acknowledgement_id = IssuesPlusOnesService.plus_one(victim_id=volunteer_id, phone_no=phone_no,
                                                            issue_id=issue_id, name=name)
        return {'status': 'success', 'insertedId': acknowledgement_id}
