# upload_endpoint.py
from fastapi import FastAPI, File, UploadFile
import os

def create_upload_app(temp_dir: str) -> FastAPI:
    app = FastAPI()

    @app.post("/upload")
    async def upload_file(file: UploadFile = File(...)):
        file_location = os.path.join(temp_dir, file.filename)
        with open(file_location, "wb+") as buffer:
            buffer.write(await file.read())
        return {"filename": file.filename}

    return app
