class ProcessVideo():
    def __init__(self, storage):
        self.__storage = storage

    def run(self, **uploaded_video):
        video_path = self.__storage.download("foobar")