import cv2
import subprocess

def extract_audio(caminho_video, caminho_audio):
    """
    Extrai o áudio de um arquivo de vídeo usando OpenCV e ffmpeg.

    Args:
        caminho_video: Caminho para o arquivo de vídeo de entrada.
        caminho_audio: Caminho para salvar o arquivo de áudio de saída (por exemplo, "audio.mp3", "audio.wav").
    """

    try:
        # Verifica se o vídeo existe
        video = cv2.VideoCapture(caminho_video)
        if not video.isOpened():
            print("Erro: Não foi possível abrir o arquivo de vídeo.")
            return

        # Usa o ffmpeg para extrair o áudio
        comando = [
            'ffmpeg',
            '-i', caminho_video,  # Arquivo de vídeo de entrada
            '-vn',  # Desativa o processamento de vídeo
            '-acodec', 'libmp3lame',  # Codec de áudio (libmp3lame para MP3, pcm_s16le para WAV)
            '-q:a', '0',  # Qualidade do áudio (0 é a melhor qualidade para libmp3lame)
            caminho_audio  # Arquivo de áudio de saída
        ]

        subprocess.run(comando, check=True, capture_output=True, text=True)
        print(f"Áudio extraído com sucesso e salvo em: {caminho_audio}")

    except FileNotFoundError:
        print("Erro: ffmpeg não encontrado. Certifique-se de que o ffmpeg está instalado e acessível no seu PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao extrair o áudio: {e}")
        print(f"Saída do ffmpeg: {e.stderr}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        if 'video' in locals() and video.isOpened():
            video.release()

