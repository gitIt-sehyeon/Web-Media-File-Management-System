from abc import ABC, abstractmethod
from domain.metadata import Metadata

class MetadataVisitor(ABC):
    @abstractmethod
    def visit_image(self, file: "File") -> Metadata:
        pass

    @abstractmethod
    def visit_video(self, file: "File") -> Metadata:
        pass

    @abstractmethod
    def visit_audio(self, file: "File") -> Metadata:
        pass