from ports.metadata_visitor import MetadataVisitor
from domain.file import File
from domain.metadata import Metadata

class ImageVisitor(MetadataVisitor):
    def visit_image(self, file: File) -> Metadata:
        return Metadata({"resolution": "1920x1080"})
    
    def visit_video(self, file: File) -> Metadata:
        raise NotImplementedError("ImageVisitor does not support video files")

    def visit_audio(self, file: File) -> Metadata:
        raise NotImplementedError("ImageVisitor does not support audio files")