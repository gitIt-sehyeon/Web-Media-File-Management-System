from fastapi import FastAPI, UploadFile, File as FastAPIFile, HTTPException
from uuid import uuid4
from datetime import datetime

# Import from your actual modules
from adapters.repositories.local_repo import LocalFileRepository
from adapters.strategies.old_file_strategy import OldFileStrategy
from domain.file import File
from domain.file_type import FileType  # Assuming you have a FileType enum
from adapters.visitors.image_visitor import ImageVisitor  # Assuming this is the correct visitor for images
from services.file_service import FileService

app = FastAPI()

# === Initialize services ===
repo = LocalFileRepository()
strategy = OldFileStrategy(days_threshold=0)
visitor = ImageVisitor()
service = FileService(repo=repo, strategy=strategy)
service.visitor = visitor  # attach visitor

@app.post("/upload/")
async def upload_file(file: UploadFile = FastAPIFile(...)):
    filename = file.filename

    if filename.endswith(".jpg") or filename.endswith(".png"):
        filetype = FileType.IMAGE
    elif filename.endswith(".mp4"):
        filetype = FileType.VIDEO
    elif filename.endswith(".mp3"):
        filetype = FileType.AUDIO
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    size = 123456  # You can read from file.file.read() if needed
    created_at = datetime.now()

    domain_file = File(
        id=uuid4(),
        filename=filename,
        filetype=filetype,
        size=size,
        created_at=created_at
    )

    service.upload(domain_file)
    return {"message": f"{filename} uploaded successfully."}


@app.get("/files/")
def list_files():
    files = repo.list()
    return [
        {
            "id": str(f.id),
            "filename": f.filename,
            "filetype": f.filetype.value,
            "created_at": f.created_at.isoformat(),
            "metadata": f.metadata.data
        }
        for f in files
    ]


@app.post("/cleanup/")
def trigger_cleanup():
    service.cleanup()
    return {"message": "Cleanup complete."}
