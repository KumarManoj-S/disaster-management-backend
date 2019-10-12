from app.main.dtos.volunteer import Volunteer
from app.main.mongo.volunteers import VolunteersService as VolunteersDBService


class VolunteersService:
    @staticmethod
    def add_new_volunteer(volunteer):
        volunteer = Volunteer(volunteer)
        volunteer_id = VolunteersDBService.store(volunteer.to_json())
        return str(volunteer_id)
