from app.main.dtos.donor import Donor
from app.main.dtos.volunteer import Volunteer
from app.main.mongo.donor import DonarsService as DonarsDBService


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
