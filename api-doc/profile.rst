Profile
*********

Profile endpoints list.

Endpoints:
    * /api/users/
    * /api/users/<USERNAME>
    * /api/users/login/
    * /api/users/logout/

Registration
--------------------------------------

Method: **POST**

Endpoint: /api/users/

Example Request::

    POST: /api/users/

    {
    "password": "123123",
    "email": "sual@sual.com",
    "username": "sualtest"
    }

Response::

    HTTP 201 Created

    {
        "id": 2,
        "username": "sualtest",
        "email": "sual@sual.com",
        "token": "6904*******5e4bb15*********53c0e840"
    }

Get User Details
--------------------------------------

Method: **GET**

Endpoint: /api/users/<USERNAME>

Example Request::

    GET: /api/users/tolgahanuzun122

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]


Response::

    HTTP 200 

    {
    "user_details": {
        "user": {
            "id": 8,
            "username": "tolgahanuzun122",
            "email": "tolgahanuzun1222@gmail.com",
            "date_joined": "2017-12-15T11:45:39.739057Z"
        },
        "company": "Just",
        "tittle": "Python"
    },
    "questions_details": {
        "id": 6,
        "body": "New answer create2r",
        "date_created": "2017-12-15T12:40:54.531281Z"
    }
    }


Login
--------------

Method: **POST**

Endpoint: /api/users/login/

Example Request::

    POST: /api/users/login/

    {
    "username": "sualtest",
    "password": "123123"
    }

Response::

    HTTP 200 OK

    {
        "auth_token": "a48dd86719fd289e7b58cb8ef776fa495ac5c358"
    }

Logout
-----------------

Method: **POST**

Endpoint: /api/users/logout/

Example Request::

    POST: /api/users/logout/
    
    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]
    
Response::

    HTTP 200: OK