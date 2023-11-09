import secrets
import hashlib
from fastapi import File
from typing import List
from celery_worker import file_handler_task


def generate_random_hash(length: int = 16) -> str:
    random_bytes = secrets.token_bytes(length)
    return hashlib.sha256(random_bytes).hexdigest()


class FileUpload:
    @staticmethod
    def upload_files(files_list: List[File]) -> int:
        for i, f in enumerate(files_list):
            with open(f'data/temp_{generate_random_hash()}', 'wb') as file_object:
                file_object.write(f.file.read())
                file_handler_task.delay(file_object.name)
        return len(files_list)


