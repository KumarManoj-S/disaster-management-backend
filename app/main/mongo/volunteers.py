from app.main.mongo.mongo import MongoConnection


class VolunteersService:
    collection_name = 'volunteers'

    @staticmethod
    def get_volunteers_collection():
        return MongoConnection.get_collection(VolunteersService.collection_name)

    @staticmethod
    def store(volunteer):
        volunteer_collection = VolunteersService.get_volunteers_collection()
        print(volunteer)
        insert_one_result = volunteer_collection.insert_one(volunteer)

        if insert_one_result.acknowledged:
            return insert_one_result.inserted_id

        raise Exception('MONGODB_ERROR')
