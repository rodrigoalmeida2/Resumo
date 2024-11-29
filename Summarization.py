import whisper
import yt_dlp
import os
from transformers import pipeline
from huggingface_hub import login
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Classe principal do processo de resumo de vídeos
class VideoSummarizer:
    def __init__(self, token):
        # Login no Hugging Face
        login(token=token)
        # Inicializa os modelos
        self.transcription_model = whisper.load_model("small")
        self.summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
    
    @staticmethod
    def download_audio(video_url, output_filename="audio"):
        """Baixa o áudio de um vídeo do YouTube."""
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Áudio baixado como {output_filename}.mp3")

    def transcribe_audio(self, audio_file):
        """Transcreve o áudio usando o modelo Whisper."""
        result = self.transcription_model.transcribe(audio_file)
        print("Transcrição concluída.")
        return result["text"]

    @staticmethod
    def split_text(text, max_tokens):
        """Divide um texto em partes menores."""
        words = text.split()
        parts = []
        current_part = []
        current_length = 0

        for word in words:
            current_length += len(word) + 1  # Inclui o espaço
            if current_length > max_tokens:
                parts.append(' '.join(current_part))
                current_part = [word]
                current_length = len(word) + 1
            else:
                current_part.append(word)
        parts.append(' '.join(current_part))
        return parts

    def summarize_text(self, text, max_tokens=1024):
        """Gera um resumo para o texto dado."""
        parts = self.split_text(text, max_tokens)
        summaries = []
        for part in parts:
            input_length = len(part.split())
            max_len = max(30, int(0.5 * input_length))  # Garantir que max_length seja no mínimo 30
            summary = self.summarization_pipeline(part, max_length=max_len, min_length=10, do_sample=False)[0]['summary_text']
            summaries.append(summary)
        print("Resumo gerado.")
        return summaries

    def process_video(self, video_url):
        """Processa o vídeo: download, transcrição e resumo."""
        audio_file = "audio.mp3"
        try:
            self.download_audio(video_url)
            transcription = self.transcribe_audio(audio_file)
            summaries = self.summarize_text(transcription)
            return summaries
        finally:
            if os.path.exists(audio_file):
                os.remove(audio_file)
                print(f"Arquivo temporário {audio_file} removido.")

# Inicialização do processo
if __name__ == "__main__":
    token = os.getenv('ACCESS_TOKEN')  # Token da API
    video_url = "https://youtu.be/-VgHk7UMPP4"

    summarizer = VideoSummarizer(token)
    summaries = summarizer.process_video(video_url)

    print("Resumo Final:")
    print(summaries)

