PP6RemoteAPI Client
===================

A client for the ProPresenter Remote Websocket API.

Getting started
---------------
```python
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
```

#### Available items
##### Library
* _presentations_: all available Presentations
* _paths_: all paths from current available Presentations
##### Presentation
* _to_slide(n)_: Go to slide _n_
* _next_slide()_: Go to next slide
* _previous_slide()_: Go to previous slide
* _current_slide()_: Returns current slide index
