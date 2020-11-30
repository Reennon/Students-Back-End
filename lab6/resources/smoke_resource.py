from flask_restful import Resource
import main

class SmokeResorces(Resource):
    """
    GET endpoint handler to test the process
    """

    def get(self):

        student = {
            "id": 34,
            "group":'214',
            "firstname": "smfffoke",
            "lastname": "smodddke"
        }
        data = main.Student(student['id'] ,student['group'],student["firstname"],student["lastname"])
        main.db.session.add(data)
        main.db.session.commit()
        return 'Hello'

