from uuid import UUID
from typing import List
from domain.file import File
from ports.file_repository import FileRepository

class LocalFileRepository(FileRepository):
    def __init__(self):
        self.files = {}

    def save(self, file: File) -> None:
        self.files[file.id] = file

    def delete(self, file: File) -> None:
        self.files.pop(file.id, None)

    def get(self, id: UUID) -> File:
        return self.files[id]

    def list(self) -> List[File]:
        return list(self.files.values())

