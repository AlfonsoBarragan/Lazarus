
# Import section
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

def save_to_mp3(msg, title):
    tts = gTTS(msg, lang='es-us')
    tts.save(f'{title}.mp3')

def reproduce_sound(filename):
    data = open('{filename}.mp3', 'rb').read()
    song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
    play(song)


mensajes = ['Hola buenos días, Higinio', 'Higinio se te ha olvidado tomarte la codeina',
            'Higinio no se te olvide cerrar la ventana que ya refresca', 
            'Higinio viene el niño a las dos y media a comer, saca el tupper del congelador',
            'Higinio apaga el horno que se te ha quedado encendido']

for msg in mensajes:
    save_to_mp3(msg, f'sound/{msg}')
