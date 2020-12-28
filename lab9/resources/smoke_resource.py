from flask_restful import Resource
import main

"""
Route "/smoke"
"""


class SmokeResources(Resource):
    """
    GET endpoint handler to test the process
    """

    def get(self):
        '''student = {
            "id": 34
            , "group": '214'
            , "first_name": "roman"
            , "last_name": "roman"
        }
        data = main.Student(
            student['id']
            , student['group']
            , student["first_name"]
            , student["first_name"]
        )
        main.db.session.add(data)
        main.db.session.commit()'''
        return 'Hello', 200
