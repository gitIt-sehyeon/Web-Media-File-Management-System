from ports.metadata_visitor import MetadataVisitor
from domain.file import File
from domain.metadata import Metadata

class AudioVisitor(MetadataVisitor):
    def visit_audio(self, file: File) -> Metadata:
        return Metadata({"bitrate": "320kbps"})
    
    def visit_image(self, file: File) -> Metadata:
        raise NotImplementedError("AudioVisitor does not support image files")
    
    def visit_video(self, file: File) -> Metadata:
        raise NotImplementedError("AudioVisitor does not support video files")