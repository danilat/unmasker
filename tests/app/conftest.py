from unittest.mock import Mock
import pytest
from unmasker.app.process_video import ProcessVideo

@pytest.fixture()
def process_video(storage):
    return ProcessVideo(storage).run

@pytest.fixture()
def storage():
    storage = Mock()
    storage.download = Mock(return_value="sample.mov")
    return storage