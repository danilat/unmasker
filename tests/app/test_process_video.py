

def test_process_video_should_read_the_file(process_video, storage):
    process_video(video_id = "video id", storage_key = "a path")

    storage.download.assert_called_with("a path")