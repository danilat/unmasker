from unmasker.app.video import Video

VIDEO_ID = "video id"
STORAGE_KEY = "a storage path"

def test_download_video_should_read_the_file(download_video, storage):
    download_video(video_id = VIDEO_ID, storage_key = STORAGE_KEY)

    storage.download.assert_called_with(STORAGE_KEY)
    
def test_download_video_should_persist_the_video_as_received(download_video, video_repository):
    download_video(video_id = VIDEO_ID, storage_key = STORAGE_KEY)

    video_repository.save.assert_called()
    persisted_video = video_repository.save.call_args.args[0]
    assert persisted_video.external_video_id == VIDEO_ID
    assert persisted_video.storage_key == STORAGE_KEY    
    assert persisted_video.is_received()
