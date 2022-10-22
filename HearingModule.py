'''
En este módulo se agregaran lo necesario para las funcionalidades de escucha 
del gestor asistencial pasivo lazarus.
'''

import whisper

def load_whisper(model_kind="base"):
    return whisper.load_model(model_kind)

def prepare_audio(sound_input):
    audio = whisper.load_audio("sound/sabina.mp3")
    audio = whisper.pad_or_trim(audio)


# load audio and pad/trim it to fit 30 seconds


# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(language="es", without_timestamps=True, fp16 = False)
result = whisper.decode(model, mel, options)
print(result.text)