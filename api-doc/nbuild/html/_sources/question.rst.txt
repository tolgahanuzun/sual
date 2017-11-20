Question
*********

Question endpoints list.

Endpoints:
    * /api/questions/
    * /api/questions/me/
    * /api/questions/<id>/

Crete
--------------------------------------

Method: **POST**

Endpoint: /api/questions/

Example Request::

    POST: /api/questions/

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
        "date_created": "2017-11-20T12:37:55.054243Z"
    }

List
--------------------------------------

Method: **GET**

Endpoint: /api/questions/

Example Request::

    GET: /api/questions/
    
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
            "date_created": "2017-10-31T13:09:35.500606Z"
        },
        {
            "user": {
                "id": 2,
                "username": "hakan",
                "email": "1@2.com",
                "date_joined": "2017-10-31T12:40:25.664074Z"
            },
            "body": "Soru -2",
            "date_created": "2017-10-31T13:09:47.363813Z"
        }
    ]

List Me
------------------

Method: **GET**

Endpoint: /api/questions/me/

Example Request::

    GET: /api/questions/me/

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
            "date_created": "2017-11-20T12:37:55.054243Z"
        },
        {
            "user": {
                "id": 1,
                "username": "tolgahan",
                "email": "2@1.com",
                "date_joined": "2017-10-31T12:39:12.097455Z"
            },
            "body": "Soru -1",
            "date_created": "2017-10-31T13:09:35.500606Z"
        }
    ]

Detail
-----------------

Method: **GET**

Endpoint: /api/questions/<id>/

Example Request::

    GET: /api/questions/3/

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
        "date_created": "2017-11-20T12:37:55.054243Z"
    }
