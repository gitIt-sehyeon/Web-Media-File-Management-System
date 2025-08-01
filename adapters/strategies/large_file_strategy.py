from ports.cleanup_strategy import CleanupStrategy
from domain.file import File

class LargeFileStrategy(CleanupStrategy):
    def __init__(self, size_threshold: int):
        self.size_threshold = size_threshold  # bytes

    def should_delete(self, file: File) -> bool:
        return file.size > self.size_threshold