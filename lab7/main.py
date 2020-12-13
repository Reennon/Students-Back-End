import hashlib

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flask import jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)



db = SQLAlchemy()

def create_app():
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """

    app = Flask(__name__)
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] =\
        r"sqlite:///D:/Documents/AppliedProgramming/lab7/database/students_database.db"
    app.config['JWT_SECRET_KEY'] = "Roman"
    jwt = JWTManager(app)
    db.init_app(app)


    register_resource(api)

    return app





def register_resource(api):
    from resources.smoke_resource import SmokeResorces
    from resources.discipline_resource import DisciplineResource
    from resources.marks_resource import MarksResource
    from resources.rating_resource import RatingResource
    from resources.student_resource import StudentResource
    from resources.login_resource import LoginResource
    """
    Connect to API rotes resources
    args:
        api: API which connect the resources routes
    Returns:
         None
    """
    api.add_resource(SmokeResorces, "/smoke")
    api.add_resource(DisciplineResource, "/disciplines")
    api.add_resource(MarksResource, "/marks")
    api.add_resource(RatingResource, "/rating")
    api.add_resource(StudentResource, "/student")
    api.add_resource(LoginResource, "/login")
    #api.add_resource(DisciplineResource, "/disciplines/<int:id>")





class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MarksID = db.Column(db.Integer, db.ForeignKey('rating.MarksID'))
    DisciplineID = db.Column(db.Integer,db.ForeignKey('disciplines.id'), nullable=False)
    Mark = db.Column(db.Integer,nullable= False)
    Passed = db.Column(db.Boolean, nullable=False)

    def __init__(self, id,disceplineID , mark , passed):
        self.id = id
        self.DisciplineID=disceplineID
        self.Mark =mark
        self.Passed = passed


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    MarksID = db.Column(db.Integer, db.ForeignKey('marks.MarksID'), nullable=False)

    def __init__(self, id, studentID,marksID):
        self.id = id
        self.StudentID=studentID
        self.MarksID =marksID


class Disciplines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Credits = db.Column(db.Integer, nullable=False)
    DisciplineName = db.Column(db.String(50), nullable=False)

    def __init__(self, id, credits, disciplineName):
        self.id = id
        self.Credits=credits
        self.DisciplineName =disciplineName

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Group = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)

    def __init__(self, id, group, lastName, firstName):
        self.id = id
        self.Group = group
        self.LastName = lastName
        self.FirstName = firstName

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    RightsID = db.Column(db.Integer, db.ForeignKey('rights.id'))
    def __init__(self, id, username, password, RightsID):
        self.id = id
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.RightsID = RightsID


class Rights(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aspect = db.Column(db.Boolean, nullable=False)
    edit = db.Column(db.Boolean, nullable=False)
    link = db.Column(db.Boolean, nullable=False)

    def __init__(self, id, aspect, edit, link):
        self.id = id
        self.aspect = aspect
        self.edit = edit
        self.link = link