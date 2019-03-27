PP6RemoteAPI Client
===================

A client for the ProPresenter6 Remote Websocket API.

Getting started
---------------

Install with ``pip``:

.. code:: bash

   $ pip install PP6RemoteAPI

Then:

.. code:: python

   from PP6RemoteAPI import PP6RemoteAPIClient as PP6
   client = PP6(host='192.168.0.100', port=54321, password='password')

   # Get first presentation in the library
   presentation = client.library.presentations[0]
   # Go to the first slide
   presentation.to_slide(0)

   # Get first clocks
   clock = client.clocks[0]
   # Set time to 5 minutes
   clock.set_time('00:05:00')
   # Start timer
   clock.start()

Find more information in the repo_

.. _repo: https://github.com/kikeh/PP6RemoteAPI
