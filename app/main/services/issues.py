from app.main.dtos.coordinate import Coordinate
from app.main.dtos.issue import Issue
from app.main.mongo.issues import IssuesService as IssuesDBService
from app.main.mongo.issues_acknowledgements import IssuesAcknowledgementsService
from app.main.mongo.issues_plus_one import IssuesPlusOneService
from app.main.mongo.victims import VictimsService
from app.main.mongo.volunteers import VolunteersService


class IssuesService:
    @staticmethod
    def add_new_issue(issue):
        issue_dto = Issue(issue)
        issue_id = IssuesDBService.add_issue(issue_dto.to_json())
        return str(issue_id)

    @staticmethod
    def get_all_issues(coordinate):
        if not coordinate:
            issues = IssuesDBService.get_all()
        else:
            issues = IssuesService.get_issues_based_on_location(coordinate)
        return issues

    @staticmethod
    def get_issue_by_id(issue_id):
        issue = IssuesDBService.get_by_id(issue_id)
        acknowledged_volunteers = IssuesAcknowledgementsService.get_all_acknowledgements_for_the_issue(issue_id)
        volunteer_ids = [acknowledged_volunteer['volunteer_id'] for acknowledged_volunteer in acknowledged_volunteers]
        volunteers = list()
        for volunteer_id in volunteer_ids:
            volunteers.append(VolunteersService.get_by_id(volunteer_id))
        issue['acknowledgedVolunteers'] = volunteers
        plus_one_victims = IssuesPlusOneService.get_all_plus_ones_for_the_issue(issue_id)
        total_plus_ones = len(plus_one_victims)
        verified_plus_one_victim_ids = [
            plus_one_victim.get('victim_id')
            for plus_one_victim in plus_one_victims
            if plus_one_victim.get('victim_id')
        ]
        victims = list()
        for victim_id in verified_plus_one_victim_ids:
            victims.append(VictimsService.get_by_id(victim_id))
        issue['plusOnes'] = {
            "totalPlusOnes": total_plus_ones,
            "anonymousPlusOnes": total_plus_ones - len(victims),
            "verifiedPlusOnes": len(victims),
            "verifiedPlusOneVictims": victims,
        }
        return issue

    @staticmethod
    def get_issues_based_on_location(coordinate):
        coordinate_dto = Coordinate(coordinate)
        issues = IssuesDBService.get_all_issues_based_on_coordinates(coordinate_dto)
        return issues

    @staticmethod
    def get_clustors_of_issues(coordinate):
        coordinate = Coordinate(coordinate)
        clustors_of_issues = IssuesDBService.get_clusters(coordinate)
        return clustors_of_issues
