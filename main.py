import whisper, yt_dlp, os
from transformers import pipeline
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

def dividir_texto(texto, max_tokens):
    palavras = texto.split()
    partes = []
    parte_atual = []
    comprimento_atual = 0

    for palavra in palavras:
        comprimento_atual += len(palavra) + 1  # Incluindo espaços
        if comprimento_atual > max_tokens:
            partes.append(' '.join(parte_atual))
            parte_atual = [palavra]
            comprimento_atual = len(palavra) + 1
        else:
            parte_atual.append(palavra)
    partes.append(' '.join(parte_atual))  # Adiciona a última parte
    return partes


def text_Gen(texto, max_tokens):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Divida o texto (assumindo que a função dividir_texto foi definida)
    partes = dividir_texto(texto, max_tokens)

    resumos = []
    for parte in partes:
        input_length = len(parte.split())  # Conta o número de palavras (ou tokens)
        max_len = max(30, int(0.5 * input_length))  # Garantir que max_length seja no mínimo 30
        resumos.append(summarizer(parte, max_length=max_len, min_length=10, do_sample=False)[0]['summary_text'])
   
    return resumos

def main(video_url):
    download_audio(video_url)
    trans = transcricao()
    print(text_Gen(trans, 1024))
    os.remove('audio.mp3')

main("https://youtu.be/-VgHk7UMPP4")
