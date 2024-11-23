import whisper
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import yt_dlp

# Função para baixar o áudio
def download_audio(url, output_filename="audio"):
    ydl_opts = {
        'format': 'bestaudio/best',  # Escolhe o melhor formato de áudio disponível
        'outtmpl': output_filename,  # Nome do arquivo de saída
        'postprocessors': [{  # Conversão do áudio para formato específico (se necessário)
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Define o formato do áudio (mp3 neste caso)
            'preferredquality': '192',  # Define a qualidade do áudio (opcional)
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def transcricao():
    modelo = whisper.load_model("small")
    result = modelo.transcribe("audio.mp3")
    return result["text"]

def Summa(pt_to_en):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    ARTICLE = pt_to_en

    print(summarizer(ARTICLE, max_length=200, min_length=50, do_sample=False))

def main():
    trans = transcricao()
    #PT_to_EN(trans)
    Summa(trans)
    # URL do vídeo do qual você quer baixar o áudio
    video_url = "https://youtu.be/GVTBZfeTDfU"

    # Baixar o áudio
    download_audio(video_url)

    print(f"Download concluído. O áudio foi salvo como 'audio.mp3'")
main()