Question
*********

Question endpoints list.

Endpoints:
    * /api/question/
    * /api/question/me/
    * /api/question/<id>/

Crete
--------------------------------------

Method: **POST**

Endpoint: /api/question/

Example Request::

    POST: /api/question/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
        {"key":"Content-Type","value":"application/json"}]

    Body:{"body":"New questions",}


Response::

    HTTP 201: Created

    {
        "user": {
            "id": 1,
            "username": "tolgahan",
            "email": "2@1.com",
            "date_joined": "2017-10-31T12:39:12.097455Z"
        },
        "body": "New questions",
        "date_created": "2017-11-20T12:37:55.054243Z",
        "id": 3
    }

List
--------------------------------------

Method: **GET**

Endpoint: /api/question/

Example Request::

    GET: /api/question/
    
    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]

Response::

    HTTP 200: Ok

    [
        {
            "user": {
                "id": 1,
                "username": "tolgahan",
                "email": "2@1.com",
                "date_joined": "2017-10-31T12:39:12.097455Z"
            },
            "body": "Soru -1",
            "date_created": "2017-10-31T13:09:35.500606Z",
            "id": 1
        },
        {
            "user": {
                "id": 2,
                "username": "hakan",
                "email": "1@2.com",
                "date_joined": "2017-10-31T12:40:25.664074Z"
            },
            "body": "Soru -2",
            "date_created": "2017-10-31T13:09:47.363813Z",
            "id": 2
        },
        {
        "user": {
            "id": 1,
            "username": "tolgahan",
            "email": "2@1.com",
            "date_joined": "2017-10-31T12:39:12.097455Z"
        },
        "body": "New questions",
        "date_created": "2017-11-20T12:37:55.054243Z",
        "id": 3
    }
    ]

List Me
------------------

Method: **GET**

Endpoint: /api/question/me/

Example Request::

    GET: /api/question/me/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
        {"key":"Content-Type","value":"application/json"}]
    

Response::

    HTTP 200: Ok

    [
        {
            "user": {
                "id": 1,
                "username": "tolgahan",
                "email": "2@1.com",
                "date_joined": "2017-10-31T12:39:12.097455Z"
            },
            "body": "New questions",
            "date_created": "2017-11-20T12:37:55.054243Z",
            "id": 3
        },
        {
            "user": {
                "id": 1,
                "username": "tolgahan",
                "email": "2@1.com",
                "date_joined": "2017-10-31T12:39:12.097455Z"
            },
            "body": "Soru -1",
            "date_created": "2017-10-31T13:09:35.500606Z",
            "id": 1
        }
    ]

Detail
-----------------

Method: **GET**

Endpoint: /api/question/<id>/

Example Request::

    GET: /api/question/3/

Response::

    HTTP 200: Ok

    {
        "user": {
            "id": 1,
            "username": "tolgahan",
            "email": "2@1.com",
            "date_joined": "2017-10-31T12:39:12.097455Z"
        },
        "body": "New questions",
        "date_created": "2017-11-20T12:37:55.054243Z",
        "id": 3
    }
