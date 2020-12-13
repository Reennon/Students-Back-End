from flask_restful import Resource
from flask import jsonify, request
from main import db, Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from main import Student

class StudentResource(Resource):
    """
    GET endpoint to get rating of the students in desc order in json format
    """
    @jwt_required
    def get(self):
        #print()
        #db.session.commit()
        #result =
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
            return "you don't have the permission to edit"

        json = request.get_json()
        return [{column: value for column, value in rowproxy.items()} for rowproxy in db.session.execute(f'''
            Select StudentID
                , "Group"
                , FirstName
                , LastName
                , sum(mrk.Mark*(dpn.Credits*1.0))
            From student as stt
                , rating as rtg
                , disciplines as dpn
                , marks as mrk
            
            Where stt.id = {json['id']}
                And rtg.MarksID = mrk.id''')]

    """
    POST endpoint to add a new student in our db
    """

    def post(self):

        json = request.get_json()
        db.session.execute(f'''
            Insert Into student(

                "Group"
                , FirstName
                , LastName
            )
            Values(
                    '{json['Group']}'
                   , '{json['FirstName']}'
                   , '{json['LastName']}'
            ); ''')
        db.session.commit()
        return rf"Nice, we' ve just registered a new Student in our db! {id}", 200


    def put(self):
        #id = request.args.get('student_id')
        json = request.get_json()
        id = json[id]
        if id < 0 or Student.query.filter_by(id = id).first() is not None:
            return "Wrong id", 403
        db.session.execute(f'''
            Update student
            Set
                "Group" = {json['Group']}
                , LastName = {json['LastName']}
                , FirstName= {json['FirstName']}
            Where id = {id};''')
        db.session.commit()
        return 'Info Updated Successfully', 200