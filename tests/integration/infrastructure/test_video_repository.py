import pytest
from unmasker.infrastructure.video_repository import VideoRepository
from unmasker.app.video import Video

@pytest.mark.integration
def test_video_repository_saves_and_returns_video():
    video_repository = VideoRepository()

    expected_external_video_id = "test_external_video_id"
    expected_storage_key = "test_storage_key"

    video = Video(external_video_id = expected_external_video_id, storage_key = expected_storage_key)
    video_repository.save(video)

    result = video_repository.get(expected_external_video_id)

    assert result.external_video_id == expected_external_video_id
    assert result.storage_key == expected_storage_key

@pytest.mark.integration
def test_video_repository_returns_nothing_if_video_not_found():
    video_repository = VideoRepository()

    not_found_key = "test_external_video_id"

    result = video_repository.get(not_found_key)

    assert result is None
