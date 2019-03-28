PP6RemoteAPI Client
===================

A client for the ProPresenter6 Remote Websocket API.

## Index
* [Getting started](#getting-started)
* [Client](#client)
  * [Functions](#functions)
  * [Properties](#properties)
* [Available items](#available-items)
  * [Audio](#audio)
  * [Clock](#clock)
  * [Library](#library)
  * [FrontMessage](#frontmessage)
  * [Playlist](#playlist)
  * [PlaylistItem](#playlistitem)
  * [Presentation](#presentation)
  * [StageDisplay](#stagedisplay)

## Getting started
Install with `pip`:
```bash
$ pip install PP6RemoteAPI
```

Then:
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

## Client
### Functions
#### _authenticate()_
Authenticates server with given credentials
#### _async_send(command, expect_response)_
Send _command_ asynchronously and waits if _expect_response_ is `True`
#### _clear_all()_
Clears all elements on live screen
#### _clear_background()_
Clears only background on live screen
#### _clear_to_logo()_
Clears all elements on live screen and goes to logo if set
#### _clear_text()_
Clears text layer on live screen
#### _clear_audio()_
Clears audio from player
#### _clear_props()_
Clears props on live screen
#### _stage_display_sets()_
Returns all available StageDisplay sets
#### _stage_display_set_display_by_name(name)_
Sets as current StageDisplay the one corresponding to _name_
#### _stage_display_set_display(index)_
Sets as current StageDisplay the one corresponding to _index_
#### _telestrator_settings()_
Returns current telestrator settings (Telestrator is not implemented in the current version).
### Properties
#### _current_presentation_
Returns current Presentation
#### _current_audio_
Returns current audio
#### _current_stage_display_
Returns current StageDisplay
#### _library_
Returns Library
#### _playlists_
Returns all available Playlists
#### _audio_playlists_
Returns all available audio Playlists
#### _front_messages_
Returns all available FrontMessages
#### _clocks_
Returns all available Clocks
#### _stage_displays_
Returns all available StageDisplays

## Available items
### Audio
#### _play()_
Start playing the selected song
#### _play_pause()_
Play/Pause the current song
### Clock
#### _settings_
Returns the current settings of the clock
#### _update(settings)_
Updates (partially or totally) the settings of the clock
#### _set_time(time)_
Sets the time of the clock. Must be of format: HH:MM:SS
#### _start()_
Starts the clock timer
#### _stop()_
Stops the clock timer
#### _reset()_
Resets the clock timer
### Library
#### _presentations_
All available Presentations
#### _paths_
All paths from current available Presentations
#### _find_presentation_by_name(name)_
Returns the Presentation in the Library with name _name_
### FrontMessage
#### _send(values)_
Sends message with the expected ordered values
#### _hide()_
Hides current message
#### _template_
Representation of the message with expected [_keys_]
### Playlist
#### _items_
PlaylistItems of the Playlist
### PlaylistItem
#### _path_
Parent path of the PlaylistItem based on the Playlists present on ProPresenter
#### _child_path_
Full path of the PlaylistItem based on the Playlists present on ProPresenter
#### _linked_element_
Expected element that is represented by the PlaylistItem. For now, only Presentations and Audios are available.
#### _type_
Type of PlaylistItem
### Presentation
#### _to_slide(n)_
Goes to slide _n_
#### _next_slide()_
Goes to next slide
#### _previous_slide()_
Goes to previous slide
#### _current_slide()_
Returns current slide index
### StageDisplay
#### _send_message(message)_
Send _message_ to the StageDisplay message panel
