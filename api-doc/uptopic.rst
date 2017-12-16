Vote and Topic
***************

Question endpoints list.

Endpoints:
    * /api/topic/
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

