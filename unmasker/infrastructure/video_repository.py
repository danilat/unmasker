from unmasker.app.video import Video

class VideoRepository:
    def __init__(self):
        self.__state = {}

    def save(self, video: Video):
        self.__state[video.external_video_id] = video
    
    def get(self, video_id: str):
        return self.__state.get(video_id, None)