from audio_extraction import *
from speech_to_text import *

# Exemplo de uso:
caminho_do_video = "media/video.mp4"  # Substitua pelo caminho do seu vídeo
caminho_do_audio = "media/audio.mp3"  # Substitua pelo caminho desejado para o arquivo de áudio
caminho_do_texto = "media/texto.txt"  # Substitua pelo caminho desejado para o arquivo de texto

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    extract_audio(caminho_do_video, caminho_do_audio)
    extract_speech(caminho_do_audio, caminho_do_texto)

