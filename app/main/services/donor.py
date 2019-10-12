from app.main.dtos.donor import Donor
from app.main.dtos.volunteer import Volunteer
from app.main.mongo.donate import DonateService
from app.main.mongo.donor import DonarsService as DonarsDBService
from app.main.services.issues import IssuesService


class DonorsService:
    @staticmethod
    def add_new_donor(donor):
        donor = Donor(donor)
        is_donor_found = DonarsDBService.get_by_phone_no(donor.phone_no)
        if not is_donor_found:
            donor_id = DonarsDBService.add_donor(donor.to_json())
        else:
            donor_id = is_donor_found['id']
        return str(donor_id)

    @staticmethod
    def get_all_donors():
        donors = DonarsDBService.get_all()
        return donors

    @staticmethod
    def get_donor(donor_id):
        volunteer = DonarsDBService.get_by_id(donor_id)
        return volunteer

    @staticmethod
    def get_donor_recommendations(issue_id):
        essentials = IssuesService.get_essentials(issue_id)
        essential_ids = [essential['id'] for essential in essentials]
        donors = DonateService.get_donor_recommendations(essential_ids)
        donor_ids = [donor['donatedBy'] for donor in donors]
        donors = list()
        for donor_id in donor_ids:
            donors.append(DonarsDBService.get_by_id(donor_id))
        return donors


