'''
En este módulo se agregaran lo necesario para las funcionalidades de sintesis
de audio y alertas para el gestor asistencial pasivo lazarus.
'''

# Import section
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

## Methods to synthesize audio

def save_custom_alert_to_mp3(msg, title):
    tts = gTTS(msg, lang='es-us')
    tts.save(f'{title}.mp3')

def reproduce_sound(filename):
    data = open('{filename}.mp3', 'rb').read()
    song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
    play(song)