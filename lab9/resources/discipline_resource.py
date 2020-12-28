from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import jsonify, request
from main import db, Users
from main import Disciplines
import json as json_tools
"""
Route "/disciplines"
"""


class DisciplineResource(Resource):
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
            return "you don't have the permission to link"
        return [{column: value for column, value in rowproxy.items()} for rowproxy in db.engine.execute(f'''
                    Select *
                    From disciplines
                    ORDER BY DisciplineName ASC ;''')], 200

    """
    POST endpoint to add a new student in our db
    """

    @jwt_required
    def post(self):

        """

        Args:
            JSON

        JSON Structure
                                TYPE        DESC
        {
            "DisciplineName":   #string
            , "Credits" :       #int
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

        json = json_tools.loads(request.get_json())
        discipline_name = json['DisciplineName']
        credits = json['Credits']
        if not link:
            return "you don't have the permission to link"
        if credits < 0:
            return "credits can`t be negative"

        db.session.execute(f'''
            Insert Into disciplines(
                 DisciplineName
                , Credits
            )
            Values(
                    '{discipline_name}'
                   , {credits}
            ); ''')
        db.session.commit()

        return rf"Nice, we' ve just added a discipline {discipline_name} to the discipline table", 200

    @jwt_required
    def put(self):

        """

        Args:
            JSO
        JSON Structure
                                TYPE        DESC
        {
            "DisciplineID":     #int
            , "DisciplineName": #string
            , "Credits" :       #int
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

        json = json_tools.loads(request.get_json())
        discipline_name = json['DisciplineName']
        credits = json['Credits']
        if not edit:
            return "you don't have the permission to edit"


        disciplineName = json['DisciplineName']
        credits = json['Credits']
        discipline_id = json['DisciplineID']
        if credits < 0:
            return "credits can`t be negative"
        if discipline_id < 0 or (Disciplines.query.filter_by(id=discipline_id).first() is None):
            return "credits can`t be negative"
        db.session.execute(f'''
            Update disciplines
            
            Set
                DisciplineName = '{disciplineName}',
                Credits = {credits}
            
            
            Where {discipline_id} = id ''')
        db.session.commit()
        return rf"Nice, we' ve just updated a discipline {disciplineName} to the discipline table", 200
