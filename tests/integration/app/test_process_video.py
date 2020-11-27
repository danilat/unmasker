import pytest
from unmasker.factory import factory


VIDEO_ID = "some_video_id"
STORAGE_KEY = "sample.mov"

@pytest.mark.integration
@pytest.mark.parametrize("video_id,storage_key", [("some_video_id","sample.mov")])
def test_process_video_is_successful_should_persist_the_video_as_processed(video_id, storage_key):
    # factory.process_videos().run(video_id = video_id, storage_key = storage_key)

    pytest.skip("pending to implement")

    
