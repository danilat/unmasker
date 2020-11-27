from dataclasses import dataclass
from enum import Enum

@dataclass
class Video:
    class Status(Enum):
        RECEIVED = 1
        PROCESSING = 2
        PROCESSED = 3
        FAILED = 4

    external_video_id: str
    storage_key: str
    status: Status = None
    unmasked_count: int = None
    failure_reason: str = None

    def is_received(self) -> bool:
        return self.status == Video.Status.RECEIVED

    def is_processing(self) -> bool:
        return self.status == Video.Status.PROCESSING

    def is_processed(self) -> bool:
        return self.status == Video.Status.PROCESSED

    def is_failed(self) -> bool:
        return self.status == Video.Status.FAILED

    def get_unmasked_count(self) -> int:
        return self.unmasked_count

    def received(self) -> None:
        self.status = Video.Status.RECEIVED

    def processing(self) -> None:
        self.status = Video.Status.PROCESSING
    
    def finished(self, count: int) -> None:
        self.status = Video.Status.PROCESSED
        self.unmasked_count = count

    def failed(self, msg: str) -> None:
        self.status = Video.Status.FAILED
        self.failure_reason = msg
