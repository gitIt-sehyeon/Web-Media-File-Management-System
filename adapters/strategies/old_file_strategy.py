from datetime import datetime, timedelta
from domain.file import File
from ports.cleanup_strategy import CleanupStrategy

class OldFileStrategy(CleanupStrategy):
    def __init__(self, days_threshold: int):
        self.days_threshold = days_threshold

    def should_delete(self, file: File) -> bool:
      age = datetime.now() - file.created_at
      #print(f"File {file.id} age: {age}, threshold: {self.days_threshold} days")
      return age > timedelta(days=self.days_threshold)