import os
import whisper
from transformers import pipeline
from huggingface_hub import login
from Download import AudioDownloader

# Classe principal do processo de resumo de vídeos
class VideoSummarizer:
    def __init__(self, token):
        # Login no Hugging Face
        login(token=token)
        # Inicializa os modelos
        self.transcription_model = whisper.load_model("small")
        self.summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
        self.audio_downloader = AudioDownloader()

    def transcribe_audio(self, audio_file):
        """Transcreve o áudio usando o modelo Whisper."""
        result = self.transcription_model.transcribe(audio_file)
        print("Transcrição concluída.")
        return result["text"]

    @staticmethod
    def split(text, max_tokens):
        """Divide o texto no limite máximo de tokens"""
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
        parts = self.split(text, max_tokens)
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
            self.audio_downloader.download(video_url)
            transcription = self.transcribe_audio(audio_file)
            summaries = self.summarize_text(transcription)
            return summaries
        finally:
            if os.path.exists(audio_file):
                os.remove(audio_file)
                print(f"Arquivo temporário {audio_file} removido.")
