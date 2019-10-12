from app.main.dtos.volunteer import Volunteer
from app.main.mongo.volunteers import VolunteersService as VolunteersDBService


class VolunteersService:
    @staticmethod
    def add_new_volunteer(volunteer):
        volunteer = Volunteer(volunteer)
        is_volunteer_found = VolunteersDBService.get_by_email(volunteer.email_id)
        if not is_volunteer_found:
            volunteer_id = VolunteersDBService.add_volunteer(volunteer.to_json())
        else:
            volunteer_id = is_volunteer_found['id']
        return str(volunteer_id)

    @staticmethod
    def get_all_volunteers():
        volunteers = VolunteersDBService.get_all()
        return volunteers

    @staticmethod
    def get_volunteer(volunteer_id):
        volunteer = VolunteersDBService.get_by_id(volunteer_id)
        return volunteer
