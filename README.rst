A simple API for presentation at WCS at SBB.

------------
Dependencies
------------
- fastapi >= 0.57.0
- uvicorn >= 0.11.5

.. code-block::bash

    $ pip install -r requirements.txt

-----------------
Run using uvicorn
-----------------

.. code-block::bash

    $ uvicorn app:main --reload