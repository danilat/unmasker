from copy import deepcopy
from unittest.mock import Mock
import pytest
from unmasker.app.process_video import ProcessVideo
from unmasker.infrastructure.storage import Storage
from unmasker.infrastructure.video_repository import VideoRepository

class CopyingMock(Mock):
    def __call__(self, /, *args, **kwargs):
        args = deepcopy(args)
        kwargs = deepcopy(kwargs)
        return super(CopyingMock, self).__call__(*args, **kwargs)

@pytest.fixture()
def process_video(storage, video_repository):
    return ProcessVideo(storage, video_repository).run

@pytest.fixture()
def storage():
    storage = Mock(spec=Storage)
    storage.download.return_value="foobar.mp4"
    return storage

@pytest.fixture()
def video_repository():
    video_repository = CopyingMock(spec=VideoRepository)
    return video_repository
