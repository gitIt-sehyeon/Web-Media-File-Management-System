from abc import ABC, abstractmethod
from typing import List
from domain.file import File
from uuid import UUID

class FileRepository(ABC):
    @abstractmethod
    def save(self, file: File) -> None:
        pass

    @abstractmethod
    def delete(self, file: File) -> None:
        pass

    @abstractmethod
    def get(self, id: UUID) -> File:
        pass

    @abstractmethod
    def list(self) -> List[File]:
        pass