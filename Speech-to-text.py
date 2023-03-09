import os
import openai
#openai.api_key = os.getenv("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")
openai.api_key = "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"
audio_file = open("Recording.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file), {
  "file": "audio.mp3",
  "model": "whisper-1",
  "response_format": "text"
}

print(transcript)

