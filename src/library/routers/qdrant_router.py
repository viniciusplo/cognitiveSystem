from dependencies import get_token_header
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.routing import APIRouter
from typing import Any
import shutil
import os

from dotenv import load_dotenv
load_dotenv()

qdrantRouter = APIRouter(
    prefix="/qdrant",
    tags=["qdrant"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@qdrantRouter.post("/insert_file")
async def insertFile(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "text/plain"]:
        raise HTTPException(status_code=400, detail="Apenas arquivos PDF ou TXT são permitidos.")
    
    file_location = f"temp/{file.filename}"
    os.makedirs("temp", exist_ok=True)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    result = insertDocument(file_path=file_location)
    return {"filename": file.filename, "message": result}

@qdrantRouter.post("/query_library")
async def query_library_endpoint(request: QueryRequest):
    result = ask(request.query)

    return result