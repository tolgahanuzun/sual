Profile
*********

The resource for liking objects. There are multiple endpoints for different object types.

Endpoints:
    * /api/users/
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

    HTTP 200: Ok

    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [{
            "id": 4,
            "full_name": "Justine Lorean",
            "first_name": "Justine",
            "small_avatar": null,
        }]
    }

Logout
-----------------

Method: **GET**

Endpoint: /api/users/logout/

Example Request::

    GET: /api/users/logout/

Response::

    HTTP 204: No Content