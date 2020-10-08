from unmasker.app.process_video import ProcessVideo
from unmasker.infrastructure.storage import Storage
from unmasker.infrastructure.video_repository import VideoRepository

class Factory:
    def __init__(self):
        self.__video_repository = VideoRepository()
        self.__storage = Storage()

    def storage(self):
        return self.__storage

    def video_repository(self):
        return self.__video_repository

    def process_videos(self):
        return ProcessVideo(self.storage(), self.video_repository())


factory = Factory()