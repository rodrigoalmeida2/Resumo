import whisper
from transformers import pipeline
import yt_dlp

# Função para baixar o áudio
def download_audio(url, output_filename="audio"):
    ydl_opts = {
        'format': 'bestaudio/best',  # Escolhe o melhor formato de áudio disponível
        'outtmpl': output_filename,  # Nome do arquivo de saída
        'postprocessors': [{  # Conversão do áudio para formato específico
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Define o formato do áudio
            'preferredquality': '192',  # Define a qualidade do áudio (opcional)
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def transcricao():
    modelo = whisper.load_model("small")
    result = modelo.transcribe("audio.mp3")
    return result["text"]

def Summa(texto):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    ARTICLE = texto

    print(summarizer(ARTICLE, max_length=500, min_length=200, do_sample=False))

def main(video_url):
    download_audio(video_url)
    trans = transcricao()
    Summa(trans)


main("https://youtu.be/GVTBZfeTDfU")