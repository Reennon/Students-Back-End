
@app.route('/user/<int:id>', methods=['POST'])
def create_user(id):

    username = request.json.get('username', None)
    firstname = request.json.get('firstname', None)
    lastname = request.json.get('lastname', None)
    password = request.json.get('password', None)

    '''
    
    create user post
    
    route: /user/<somestupidint>
    
    IN: JSON
    
    {
        "username" : "somestupidname"
        , "firstname" : "somestupidfirstname"
        , "lastname" : "somestupidlastname"
        , "password" : "somestupidpass"
    }
    
    OUT: JSONIFY STATUS
    
    '''

    if username and password and firstname and lastname :
        new_user = User(
            # start added
            iduser = id,
            # end added
            userName=username, firstName=firstname, lastName=lastname, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(status='created'), 200
    else:
        return jsonify(status='Bad data'), 204


@app.route('/user/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def userId(id):

    user = User.query.filter_by(iduser=id).first()
    if user is None:
        return jsonify(status='not found user'), 404

    if request.method == 'GET':
        return jsonify(status='current User', name=user.userName, firstname=user.firstName, lastname=user.lastName), 200

    if request.method == 'PUT':

        '''

            create user put

            route: /user/<somestupidint>

            IN: JSON

            {
                "username" : "somestupidname"
                , "firstname" : "somestupidfirstname"
                , "lastname" : "somestupidlastname"
                , "password" : "somestupidpass"
            }

            OUT: JSONIFY STATUS

            '''

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        firstname = request.json.get('firstname', None)
        lastname = request.json.get('lastname', None)

        if username and password and firstname and lastname:
            user.userName = username
            user.lastName = lastname
            user.firstName = firstname
            user.password = generate_password_hash(password)
            db.session.commit()
            return jsonify(status='updated', name=user.userName, firstname=user.firstName, lastname=user.lastName), 202
        else:
            return jsonify(status='Bad data'), 204

    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify(status='deleted', name=user.userName, firstname=user.firstName, lastname=user.lastName), 201


def login_user(username, password):  # noqa: E501
    """Logs user into the system
     # noqa: E501
    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str
    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session
     # noqa: E501
    :rtype: None
    """
    return 'do some magic!'

@app.route('/credit', methods=['POST'])
def create_credit():

    startdate = request.json.get('startdate', None)
    finishdate = request.json.get('finishdate', None)
    sum = request.json.get('sum', None)
    percent = request.json.get('percent', None)
    status = request.json.get('status', None)
    '''

                credit post request

                route /credit/<somestupidint>

                IN: JSON

                JSON STRUCTURE:

                {
                    "startdate" : "someStupidDate"
                    , "finishDate" : "someFinishdateStupid"
                    , "sum" : 32269422
                    , "percent : 99
                    , "status" : "busy"
                }

                OUT: status, code

            '''

    if startdate and finishdate and sum and percent and status :
        new_credit = Credit(startDate=startdate, finishDate=finishdate, sum=sum, percent=percent, status=status)
        db.session.add(new_credit)
        db.session.commit()
        return jsonify(status='created'), 200
    else:
        return jsonify(status='Bad data'), 204

@app.route('/credit/<int:id>', methods=['GET', 'PUT'])
def creditId(id):




    credit = Credit.query.filter_by(idcredit=id).first()
    if credit is None:
        return jsonify(status='not found user'), 404
    if request.method == 'GET':
        '''

            credit get request

            route /credit/<somestupidint>

            IN: ID in route


            OUT: JSON

        '''
        return jsonify(status='current User', startdate=credit.startDate, finishdate=credit.finishDate, sum=credit.percent, status_of_credite=credit.status), 200

    if request.method == 'PUT':

        '''

            credit put request
            
            route /credit/<somestupidint>
            
            IN: JSON
            
            JSON STRUCTURE:
            
            {
                "startdate" : "someStupidDate"
                , "finishDate" : "someFinishdateStupid"
                , "sum" : 32269422
                , "percent : 99
                , "status" : "busy"
                , "userID" : 228
                , "bankID" : 69
            }
            
            OUT: empty

        '''

        startdate = request.json.get('startdate', None)
        finishdate = request.json.get('finishdate', None)
        sum = request.json.get('sum', None)
        percent = request.json.get('percent', None)
        status = request.json.get('status', None)

        if startdate and finishdate and sum and percent and status :
            credit.startDate = startdate
            credit.finishDate = finishdate
            credit.sum = sum
            credit.percent = percent
            credit.status = status