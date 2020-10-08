# Unmasker

This is a component that comunicates with other components via events. Receives an event from other systems about video files that had been uploaded and need to be processed to identify how many people without masks appears in the videos.


The workflow expected for the component is this:
- Receives an notification about a video that an user uploaded. The event contains a video identifier and the key to the file in the storage.
- Gets the file from the type of the storage and specified path.
- Start to process the video and send an event that the video started to process.
- If some error happen unmasker should send an event about the detection was failed.
- If is a success unmasker should send an event with the information about how many people in the video appears without masks and its video identifier.

Also, for operational purposes we want to register the videos that were received by unmasker and keep up to date it's status.

## How to run

This project uses Pipenv to manage the dependencies, to install it use 

`pipenv install --dev`

And to run the test suite:

`pipenv run pytest`

If you don't want to run the integration tests execute

`pipenv run pytest -m "not integration"`

If you want to run only the integration tests execute

`pipenv run pytest -m integration`