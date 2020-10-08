from unittest.mock import Mock
import pytest
from unmasker.app.process_video import ProcessVideo
from unmasker.infrastructure.storage import Storage
from unmasker.infrastructure.video_repository import VideoRepository

@pytest.fixture()
def process_video(storage, video_repository):
    return ProcessVideo(storage, video_repository).run

@pytest.fixture()
def storage():
    storage = Mock(spec=Storage)
    return storage

@pytest.fixture()
def video_repository():
    video_repository = Mock(spec=VideoRepository)
    return video_repository