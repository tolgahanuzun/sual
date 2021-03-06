Vote and Topic
***************

Question endpoints list.

Endpoints:
    * /api/topic/
    * /api/topic/<id>/
    * /api/topics/<key>/
    * /api/votes/
    * /api/follow/topic/
    * /api/follow/topic/<id>

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




Topic search
--------------------------------------

Method: **GET**

Endpoint: /api/topics/<key>/

Example Request::

    GET: /api/topics/PyThoN/


Response::

    HTTP 200: OK

    [
    {
        "id": 1,
        "name": "Python",
        "tittle": "Python Lang",
        "about": "Python Lang Questions List",
        "image": null
    },
    {
        "id": 4,
        "name": "python data",
        "tittle": "data",
        "about": "data",
        "image": null
    }
    ]


Example Request::

    GET: /api/topics/Go2/


Response::

    HTTP 204: No Content
    {
    "result": "Topic or content not found!"
    }


Topic Get
--------------------------------------

Method: **GET**

Endpoint: /api/topic/<id>/

Example Request::

    GET: /api/topics/1/


Response::

    HTTP 200: OK

    {
    "topic_details": {
        "id": 1,
        "name": "Python",
        "tittle": "Python Lang",
        "about": "Python Lang Questions List",
        "image": null
    },
    "questions_details": [
        {
            "user": 1,
            "body": "Soru -1",
            "date_created": "2017-10-31T13:09:35.500606Z",
            "id": 1
        },
        {
            "user": 1,
            "body": "New answer create",
            "date_created": "2017-12-06T17:57:33.499951Z",
            "id": 4
        }
    ]
    }




Answer Vote
--------------------------------------

Method: **POST**

Endpoint: /api/votes/

Example Request::

    POST: /api/votes/
    
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

User Topic Follow
--------------------------------------

Method: **Post**

Endpoint: /api/follow/topic/

Example Request::

    POST: /api/follow/topic/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]
    
    Body:{"topic_id": 1}

Response::

    HTTP 201: Created

Example Request::

    POST: /api/follow/topic/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]
    
    Body:{"topic_id": 1}

Response::

    HTTP 406: NOT ACCEPTABLE


User Topic Unfollow
--------------------------------------

Method: **DELETE**

Endpoint: /api/follow/topic/

Example Request::

    DELETE: /api/follow/topic/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]
    
    Body:{"topic_id": 1}

Response::

    HTTP 204: Not Content
    

Example Request::

    DELETE: /api/follow/topic/

    Header:[{"key":"Authorization","value":"Token 5e4d6253cb7b9b19f7c8dd499c4385bb01bd4822"},
            {"key":"Content-Type","value":"application/json"}]
    
    Body:{"topic_id": 1}

Response::

    HTTP 404: Not found
    

Topic in User List
--------------------------------------

Method: **GET**

Endpoint: /api/follow/topic/<id>

Example Request::

    GET: /api/follow/topic/1


Response::

    HTTP 200: OK

    [
    {
        "user": {
            "id": 8,
            "username": "tolgahanuzun122",
            "email": "tolgahanuzun1222@gmail.com",
            "date_joined": "2017-12-15T11:45:39.739057Z"
        }
    },
    {
        "user": {
            "id": 5,
            "username": "tolgahanuzun1",
            "email": "tolgahanuzun2@gmail.com",
            "date_joined": "2017-12-15T11:43:03.737737Z"
        }
    }
    ]
