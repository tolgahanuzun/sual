Vote and Topic
***************

Question endpoints list.

Endpoints:
    * /api/topic/
    * /api/topic/<key>/
    * /api/vote/

Topic List
--------------------------------------

Method: **GET**

Endpoint: /api/topic/

Example Request::

    GET: /api/topic/


Response::

    HTTP 200: OK

    [
        {
            "id": 1,
            "name": "Python",
            "tittle": "Python Lang",
            "about": "Python Lang Questions List",
            "image": null
        }
    ]


Topic Create
--------------------------------------

Method: **POST**

Endpoint: /api/topic/

Example Request::

    POST: /api/topic/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]

    Body:
    {
    "tittle": "Python Lang",
    "about": "Python Lang Questions List",
    "image": null,
    "name": "python"
    }

Response::

    HTTP 200: OK

    [
        {
            "id": 1,
            "name": "Python",
            "tittle": "Python Lang",
            "about": "Python Lang Questions List",
            "image": null
        }
    ]

Example Request::

    POST: /api/topic/


    Body:
    {
    "tittle": "Go Lang",
    "about": "Go Lang Questions List",
    "image": null,
    "name": "Go"
    }

Response::

    HTTP 401: Unauthorized

    [
    "result": "You can not do this without signing in."
    ]   




Topic Get
--------------------------------------

Method: **GET**

Endpoint: /api/topic/<key>/

Example Request::

    GET: /api/topic/PyThoN/


Response::

    HTTP 200: OK
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "topic": 1,
                "questions": {
                    "user": 1,
                    "body": "Soru -1",
                    "date_created": "2017-10-31T13:09:35.500606Z",
                    "id": 1
                }
            }
        ]
    }


Example Request::

    GET: /api/topic/Go2/


Response::

    HTTP 204: No Content
    {
    "result": "Topic or content not found!"
    }

Answer Vote
--------------------------------------

Method: **POST**

Endpoint: /api/vote/

Example Request::

    POST: /api/vote/
    
    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]
    
    Body:{
            "answer":1,
            "type": "True"

        }

Response::

    HTTP 201: Created

    {
        "type": "True",
        "vote": 1,
        "answer": 1
    }

