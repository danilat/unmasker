from .video import Video
from unmasker.infrastructure.video_repository import VideoRepository
from .unmasked_recognizer import UnmaskedRecognizer

class ProcessVideo():
    def __init__(self, video_repository: VideoRepository, unmasked_recognizer: UnmaskedRecognizer) -> None:
        self.__video_repository = video_repository
        self.__unmasked_recognizer = unmasked_recognizer

    def run(self, video_id: str) -> None:
        video = self.__video_repository.get(video_id)        
        video.processing()        
        self.__video_repository.save(video)

        try:
            unmasked_count = self.__unmasked_recognizer.count(video)
            video.finished(unmasked_count)
        except Exception as identifier:
            video.failed(str(identifier))
        finally:
            self.__video_repository.save(video)       
        
        