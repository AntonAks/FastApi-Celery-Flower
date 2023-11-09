from fastapi import APIRouter, File, UploadFile
from typing import List
from controllers.files import FileUpload

files_router = APIRouter()


@files_router.get("/")
async def root():
    return {"message": "File Upload Example. Please use `/docs` for enter to Swagger UI and test the API"}


@files_router.post("/upload_files/")
async def upload_file_queue(files_list: List[UploadFile] = File(...)):
    files_number = FileUpload.upload_files(files_list)
    return {"Number of files will be processed": files_number}
