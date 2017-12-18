Answers
*********

The resource for liking objects. There are multiple endpoints for different object types.

Endpoints:
    * /api/answer/
    * /api/answer/<pk>/

Answer Create
--------------------------------------

Method: **POST**

Endpoint: /api/answer/

Example Request::

    POST: /api/answer/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
    {"key":"Content-Type","value":"application/json"}]

    Body:
    {
        "body":"New ask",
        "question": 2
    }

Response::

    HTTP 201 Created

    {
    "owner": {
        "id": 1,
        "username": "tolgahan",
        "email": "2@1.com",
        "date_joined": "2017-10-31T12:39:12.097455Z"
    },
    "question": {
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
    "body": "New ask",
    "date_created": "2017-12-18T22:53:40.765651Z",
    "id": 21
    }

Me Answer List
----------------

Method: **GET**

Endpoint: /api/answer/

Example Request::

    GET: /api/answer/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
    {"key":"Content-Type","value":"application/json"}]

Response::

    HTTP 200: Ok

    {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "owner": {
                "id": 1,
                "username": "tolgahan",
                "email": "2@1.com",
                "date_joined": "2017-10-31T12:39:12.097455Z"
            },
            "question": {
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
            "body": "cevap",
            "date_created": "2017-11-20T12:57:14.730609Z",
            "id": 4
        },
        {
            "owner": {
                "id": 1,
                "username": "tolgahan",
                "email": "2@1.com",
                "date_joined": "2017-10-31T12:39:12.097455Z"
            },
            "question": {
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
            "body": "New answer create2r",
            "date_created": "2017-12-06T18:23:33.065708Z",
            "id": 20
        },
        {
            "owner": {
                "id": 1,
                "username": "tolgahan",
                "email": "2@1.com",
                "date_joined": "2017-10-31T12:39:12.097455Z"
            },
            "question": {
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
            "body": "New ask",
            "date_created": "2017-12-18T22:53:40.765651Z",
            "id": 21
        }
    ]
    }

Spesifik Answer Get
-----------------------

Method: **GET**

Endpoint: /api/answer/<pk>/

Example Request::

    GET: /api/answer/2/

Response::

    HTTP 200: Ok

    {
    "owner": {
        "id": 2,
        "username": "hakan",
        "email": "1@2.com",
        "date_joined": "2017-10-31T12:40:25.664074Z"
    },
    "question": {
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
    "body": "lul",
    "date_created": "2017-10-31T13:10:28.503160Z",
    "id": 1,
    "vote": 1
    }