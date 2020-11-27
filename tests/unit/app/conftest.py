from copy import deepcopy
from unittest.mock import Mock
import pytest
from unmasker.app.process_video import ProcessVideo
from unmasker.app.download_video import DownloadVideo
from unmasker.infrastructure.storage import Storage
from unmasker.infrastructure.video_repository import VideoRepository
from unmasker.app.unmasked_recognizer import UnmaskedRecognizer

class CopyingMock(Mock):
    def __call__(self, /, *args, **kwargs):
        args = deepcopy(args)
        kwargs = deepcopy(kwargs)
        return super(CopyingMock, self).__call__(*args, **kwargs)

@pytest.fixture()
def download_video(storage, video_repository):
    return DownloadVideo(storage, video_repository).run

@pytest.fixture()
def unmasked_recognizer():
    unmasked_recognizer = CopyingMock(spec=UnmaskedRecognizer)
    unmasked_recognizer.count.return_value = 200
    return unmasked_recognizer

@pytest.fixture()
def process_video(video_repository, unmasked_recognizer):
    return ProcessVideo(video_repository, unmasked_recognizer).run

@pytest.fixture()
def storage():
    storage = Mock(spec=Storage)
    storage.download.return_value = "foobar.mp4"
    return storage

@pytest.fixture()
def video_repository():
    video_repository = CopyingMock(spec=VideoRepository)
    return video_repository
