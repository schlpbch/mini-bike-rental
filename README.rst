A simple API for presentation at WCS workshop at SBB. The creaded YAML file is under the openapi_ folder

The implmentation use the _FastApi: https://fastapi.tiangolo.com/ framework which is fast&fun to work with.


------------
Dependencies
------------
- fastapi >= 0.57.0
- uvicorn >= 0.11.5

.. code-block:: bash

    $ pip install -r requirements.txt

-----------------
Run using uvicorn
-----------------

.. code-block:: bash

    $ uvicorn main:app --reload