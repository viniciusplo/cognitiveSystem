from typing import List
from pydantic import BaseModel

class SpeechToTextRequestDatamodel(BaseModel):
    audio_file: str

class TextToSpeechRequestDatamodel(BaseModel):
    text: str

class SpeechToTextResponseDatamodel(BaseModel):
    transcription: str

class TextToSpeechResponseDatamodel(BaseModel):
    audio_file: str
