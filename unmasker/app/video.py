from dataclasses import dataclass
from enum import Enum

@dataclass
class Video:
    class Status(Enum):
        RECEIVED = 1

    external_video_id: str
    storage_key: str
    status: Status = None

    def is_received(self) -> bool:
        return self.status == Video.Status.RECEIVED

    def received(self):
        self.status = Video.Status.RECEIVED


