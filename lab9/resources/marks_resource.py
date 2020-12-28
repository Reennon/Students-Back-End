from flask_restful import Resource
from flask import jsonify, request
from main import db, Users
from flask_jwt_extended import jwt_required, get_jwt_identity
import json as json_tools
"""
Route "/marks"
"""


class MarksResource(Resource):
    """
    GET endpoint to get rating of the students in desc order in json format
    """

    @jwt_required
    def get(self):
        # id = request.args.get('student_id')
        current_username = get_jwt_identity()

        if Users.query.filter_by(username=current_username).first() is None:
            return 400

        rights = (([{column: value for column, value in rowproxy.items()} for rowproxy in db.session.execute(f'''
                                    Select aspect, edit, link
                                    From rights, users
                                    WHERE rights.id = users.RightsID
                                    AND users.username = '{current_username}'
                                ''')].pop(0)))
        aspect = rights['aspect']
        edit = rights['edit']
        link = rights['link']

        if not aspect:
            return "you don't have the permission to aspect", 403

        return [{column: value for column, value in rowproxy.items()} for rowproxy in db.session.execute(f'''
            Select disciplines.id
                , DisciplineName
                , Mark
                , Passed
                , Credits
            From disciplines
                , marks
                , rating
            Where 1 = marks.MarksID
                and marks.DisciplineID = disciplines.id
                and rating.MarksID = marks.MarksID
            ORDER BY Credits Desc''')], 200

    """
    POST endpoint to add a new student in our db
    """

    @jwt_required
    def post(self):
        """

            Args:
                JSON string

            JSON Structure
                                    TYPE        DESC
            {
                "MarksID":          #int
                , "DisciplineID" :  #int
                , "Mark":           #float
                , "Passed":         #boolean
            }

            Returns:
                Operation result

        """

        current_username = get_jwt_identity()

        if Users.query.filter_by(username=current_username).first() is None:
            return 400

        rights = (([{column: value for column, value in rowproxy.items()} for rowproxy in db.session.execute(f'''
                            Select aspect, edit, link
                            From rights, users
                            WHERE rights.id = users.RightsID
                            AND users.username = '{current_username}'
                        ''')].pop(0)))
        aspect = rights['aspect']
        edit = rights['edit']
        link = rights['link']

        if Users.query.filter_by(username=current_username).first() is None:
            return 400
        if not link:
            return "you don't have the permission to edit", 405
        json = json_tools.loads(request.get_json())
        marks_id = json['MarksID']
        discipline_id = json['DisciplineID']
        mark = json['Mark']
        passed = json['Passed']
        if marks_id < 0 or discipline_id < 0 or mark < 0 \
                or type(marks_id) is not int \
                or type(discipline_id) is not int \
                or type(mark) is not (int or float) \
                or type(passed) is not bool:
            return "Bad Data", 403
        db.session.execute(f'''
            Insert Into marks(
                 MarksID
                 , DisciplineID
                , Mark
                , Passed
            )
            Values(
                {marks_id}
                , {discipline_id}
                , {mark}
                , {passed}
            ); ''')
        db.session.commit()
        return 200

    @jwt_required
    def put(self):
        """

            Args:
                JSON string

            JSON Structure
                                    TYPE        DESC
            {
                'MarksID'           #int
                'DisciplineID'      #int
                'Mark'              #int
                'Passed'            #Boolean
            }

            Returns:
                Operation result

        """
        current_username = get_jwt_identity()

        if Users.query.filter_by(username=current_username).first() is None:
            return 400

        rights = (([{column: value for column, value in rowproxy.items()} for rowproxy in db.session.execute(f'''
                                    Select aspect, edit, link
                                    From rights, users
                                    WHERE rights.id = users.RightsID
                                    AND users.username = '{current_username}'
                                ''')].pop(0)))
        aspect = rights['aspect']
        edit = rights['edit']
        link = rights['link']

        if not edit:
            return "you don't have the permission to edit", 405

        json = json_tools.loads(request.get_json())
        marks_id = json['MarksID']
        discipline_id = json['DisciplineID']
        mark = json['Mark']
        passed = json['Passed']
        if marks_id < 0 or discipline_id < 0 or mark < 0 \
                or type(marks_id) is not int \
                or type(discipline_id) is not int \
                or type(mark) is not (int or float) \
                or type(passed) is not bool:
            return "Bad Data", 403
        db.session.execute(f'''
            Update marks
            Set
                 DisciplineID = {discipline_id}
                , Mark = {mark}
                , Passed = {passed}
            WHERE MarksID = {marks_id}
            ''')
        db.session.commit()
        return 200
