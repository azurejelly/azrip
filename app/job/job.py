from uuid import uuid4
from enum import Enum, auto
from ..utils import device
from os import getenv

WORK_DIR = getenv("WORK_DIR", "")

class JobFileExtension(Enum):
    FLAC = (".flac",)
    WAV = (".wav",)

    def __init__(self, ext):
        self.ext = ext

class JobState(Enum):
    FAILED = auto()
    WAITING = auto()
    RIPPING = auto()
    CONVERTING = auto()
    ZIPPING = auto()
    DONE = auto()

class Job:
    def __init__(self, name, device, file_ext=JobFileExtension.FLAC):
        self.id = str(uuid4())
        self.name = name
        self.device = device
        self.state = JobState.WAITING
        self.file_ext = file_ext
        self.message = None

    def process(self):
        dev = self.device
        job = self.id

        if device.is_busy(dev):
            self.state = JobState.FAILED
            self.message = "Device was already busy"
        else:
            device.assign(dev, job)

    def __iter__(self):
        yield "id", str(self.id)
        yield "name", self.name
        yield "device", self.device
        yield "state", self.state.name
        yield "file_ext", self.file_ext.value
        yield "message", self.message

