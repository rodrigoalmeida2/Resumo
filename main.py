import whisper, yt_dlp, os
from transformers import pipeline
import torch, transformers
from huggingface_hub import login
from dotenv import load_dotenv

load_dotenv()

login(token=os.getenv('ACCESS_TOKEN'))

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

# Transcrever o audio
def transcricao():
    modelo = whisper.load_model("small")
    result = modelo.transcribe("audio.mp3")
    return result["text"]

def text_Gen():
    model_id = "meta-llama/Meta-Llama-3-8B"

    pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")
    pipeline("Hey how are you doing today?")


def Summa(texto):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    ARTICLE = texto
    print(summarizer(ARTICLE, max_length=300, min_length=100, do_sample=False))

def main(video_url):
    download_audio(video_url)
    trans = transcricao()
    Summa(trans)
    os.remove('audio.mp3')

#main("https://youtu.be/tHPCpso-Fr0")
text_Gen()