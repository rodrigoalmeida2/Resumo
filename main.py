import whisper, yt_dlp, os
from transformers import pipeline
import transformers
import torch

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
    model_id = "meta-llama/Llama-3.2-3B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    messages = [
        {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
        {"role": "user", "content": "Who are you?"},
    ]
    outputs = pipe(
        messages,
        max_new_tokens=256,
    )
    print(outputs[0]["generated_text"][-1])




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