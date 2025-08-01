from uuid import UUID
from ports.metadata_visitor import MetadataVisitor
from domain.metadata import Metadata
from domain.file_type import FileType
from datetime import datetime

class File:
    def __init__(self, id: UUID, filename: str, filetype: FileType, size: int, created_at: datetime):
        self.id = id
        self.filename = filename
        self.filetype = filetype
        self.size = size
        self.created_at = created_at
        self.metadata: Metadata = Metadata(data={})

    def accept(self, visitor: MetadataVisitor) -> Metadata:
        if self.filetype == FileType.IMAGE:
            return visitor.visit_image(self)
        elif self.filetype == FileType.VIDEO:
            return visitor.visit_video(self)
        elif self.filetype == FileType.AUDIO:
            return visitor.visit_audio(self)
        else:
            raise ValueError(f"Unsupported file type: {self.filetype}")