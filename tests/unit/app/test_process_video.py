from unmasker.app.video import Video

VIDEO_ID = "video id"
STORAGE_KEY = "a storage path"
    
def test_process_video_should_persist_the_video_as_processing(process_video, video_repository):
    video_repository.get.return_value = Video(external_video_id = VIDEO_ID, storage_key = STORAGE_KEY)

    process_video(video_id = VIDEO_ID)

    video_repository.save.assert_called()
    persisted_video = video_repository.save.call_args_list[0].args[0]
    assert persisted_video.is_processing() == True

def test_process_video_updates_unmasked_count(process_video, video_repository, unmasked_recognizer):
    expected_value = 288
    video_repository.get.return_value = Video(external_video_id = VIDEO_ID, storage_key = STORAGE_KEY)
    unmasked_recognizer.count.return_value = expected_value
    
    process_video(video_id = VIDEO_ID)

    persisted_video = video_repository.save.call_args_list[1].args[0]
    assert persisted_video.get_unmasked_count() == expected_value
                                                                                    
def test_process_video_should_persist_the_video_as_processed(process_video, video_repository):
    video_repository.get.return_value = Video(external_video_id = VIDEO_ID, storage_key = STORAGE_KEY)

    process_video(video_id = VIDEO_ID)

    video_repository.save.assert_called()
    persisted_video = video_repository.save.call_args_list[1].args[0]
    assert persisted_video.is_processed() == True
                                                                                                
def test_process_video_should_persist_the_video_as_failed(process_video, video_repository, unmasked_recognizer):
    expected_exception_msg = "msg"
    video_repository.get.return_value = Video(external_video_id = VIDEO_ID, storage_key = STORAGE_KEY)

    unmasked_recognizer.count.side_effect = Exception(expected_exception_msg)

    process_video(video_id = VIDEO_ID)

    video_repository.save.assert_called()
    persisted_video = video_repository.save.call_args_list[1].args[0]

    assert persisted_video.is_failed() == True
    assert persisted_video.failure_reason == expected_exception_msg