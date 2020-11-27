from .video import Video

class DownloadVideo():
    def __init__(self, storage, video_repository):
        self.__storage = storage
        self.__video_repository = video_repository

    def run(self, **uploaded_video) -> str:
        video = Video(external_video_id=uploaded_video["video_id"], storage_key=uploaded_video["storage_key"])
        video.received()
        self.__video_repository.save(video)
        video_path = self.__storage.download(uploaded_video["storage_key"])
    
        return video_path
