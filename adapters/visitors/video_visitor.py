from ports.metadata_visitor import MetadataVisitor
from domain.file import File
from domain.metadata import Metadata

class VideoVisitor(MetadataVisitor):
    def visit_video(self, file: File) -> Metadata:
        return Metadata({"duration": "2min"})
    
    def visit_image(self, file: File) -> Metadata:
        raise NotImplementedError("VideoVisitor does not support image files")
    
    def visit_audio(self, file: File) -> Metadata:
        raise NotImplementedError("VideoVisitor does not support audio files")