from flask_restplus import Namespace, Resource
from flask import request

from app.main.services.volunteers import VolunteersService

api = Namespace('Volunteers', description="Endpoints to get volunteer details")


@api.route('volunteers')
class GetVictims(Resource):
    def post(self):
        volunteer = request.json
        volunteer_id = VolunteersService.add_new_volunteer(volunteer)
        return {'volunteerId': volunteer_id}
