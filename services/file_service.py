from uuid import UUID
from domain.file import File
from ports.file_repository import FileRepository
from ports.cleanup_strategy import CleanupStrategy
from adapters.visitors.image_visitor import ImageVisitor  # Assuming this is the correct visitor for images

class FileService:
    def __init__(self, repo: FileRepository, strategy: CleanupStrategy):
        self.repo = repo
        self.strategy = strategy

    def upload(self, file: File) -> None:
        file.metadata = file.accept(ImageVisitor())  # or the correct visitor
        self.repo.save(file)

    def download(self, id: UUID) -> File:
        return self.repo.get(id)

    def delete(self, id: UUID) -> None:
        file = self.repo.get(id)
        self.repo.delete(file)

    def cleanup(self) -> None:
        for file in self.repo.list():
            #print(f"Checking file {file.id} for cleanup")
            if self.strategy.should_delete(file):
                #print(f"Deleting file {file.id} as it meets cleanup criteria")
                self.repo.delete(file)