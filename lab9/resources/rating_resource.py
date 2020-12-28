from flask_jwt_extended import *
from flask_restful import Resource
from flask import jsonify, request
from main import db, Users
import json as json_tools
"""
Route "/rating"
"""


class RatingResource(Resource):
    """
    GET endpoint to get rating of the students in desc order in json format
    """

    @jwt_required
    def get(self):

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
            return "You don't have the permission to aspect", 403

        return [{column: value for column, value in rowproxy.items()} for rowproxy in db.engine.execute(f'''
                Select FirstName
                     , LastName
                     , sum(mrk.Mark*(dpn.Credits*1.0))/(count()*dpn.Credits*100) as Rating
                From rating as rtg
                    , marks as mrk
                    , disciplines as dpn
                    , student as stt
                Where stt.id = rtg.StudentID
                    And rtg.MarksID = mrk.MarksID
                    And mrk.DisciplineID = dpn.id
                Group by rtg.StudentID
                Order by Rating DESC
                Limit 100;''')], 200

    @jwt_required
    def post(self):
        """

            Args:
                JSON string

            JSON Structure
                                    TYPE        DESC
            {
                "StudentID":        #int
                , "MarksID" :       #int
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

        # print(result)

        json = json_tools.loads(request.get_json())
        student_id = json['StudentID']
        marks_id = json['MarksID']
        if not edit:
            return "You don't have the permission to edit"
        if (marks_id or student_id) < 0 or (type(marks_id) or type(student_id)) is not int:
            return "Validation fail", 403
        db.session.execute(f'''
            Insert Into rating(
                StudentID
                , MarksID
            )
            Values(
                 {student_id}
                , {marks_id}
            );''')
        db.session.commit()
        return 200
