import torch
from TTS.api import TTS
import time

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

start = time.time()
wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
tts.tts_to_file(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
end = time.time()

print(end -start)