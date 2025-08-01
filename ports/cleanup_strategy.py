from abc import ABC, abstractmethod
from datetime import datetime
from domain.file import File

class CleanupStrategy(ABC):
    @abstractmethod
    def should_delete(self, file: File) -> bool:
        pass