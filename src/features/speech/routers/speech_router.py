from dependencies import get_token_header
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.routing import APIRouter
from typing import Any
import shutil
import os
from src.features.speech.dataModels.endpoint_datamodels import SpeechToTextRequestDatamodel, TextToSpeechRequestDatamodel
from src.features.speech.controllers.speech_to_text_controller import speechToTextController
from src.features.speech.controllers.text_to_speech_controller import textToSpeechController
from dotenv import load_dotenv
load_dotenv()

speechRouter = APIRouter(
    prefix="/speech",
    tags=["speech"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@speechRouter.post("/speechToText")
async def speechToText(request: SpeechToTextRequestDatamodel):
    result = speechToTextController(request.audio_file)

    return result

@speechRouter.post("/textToSpeech")
async def textToSpeech(request: TextToSpeechRequestDatamodel):
    result = textToSpeechController(request.text)

    return result