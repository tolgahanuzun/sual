Question
*********

The resource for liking objects. There are multiple endpoints for different object types.

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

List
--------------------------------------

Method: **GET**

Endpoint: /api/questions/

Example Request::

    GET: /api/questions/

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

List Me
------------------

Method: **GET**

Endpoint: /api/questions/me/

Example Request::

    POST: /api/questions/me/

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

Detail
-----------------

Method: **GET**

Endpoint: /api/questions/<id>/

Example Request::

    GET: /api/questions/2/

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