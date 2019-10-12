from app.main.dtos.coordinate import Coordinate
from app.main.dtos.issue import Issue
from app.main.mongo.issues import IssuesService as IssuesDBService


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
