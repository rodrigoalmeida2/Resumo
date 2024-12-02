import os
import whisper
from transformers import pipeline
from huggingface_hub import login
from Download import AudioDownloader
from Divide_Texto import TextSplitter

class VideoSummarizer:
    """Classe principal do processo de resumo de vídeos."""
    
    def __init__(self, token):
        # Login no Hugging Face
        login(token=token)
        # Inicializa os modelos
        self.transcription_model = whisper.load_model("small")
        self.summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
        self.audio_downloader = AudioDownloader()
        self.text_splitter = TextSplitter()

    def transcribe_audio(self, audio_file):
        """Transcreve o áudio usando o modelo Whisper."""
        result = self.transcription_model.transcribe(audio_file)
        print("Transcrição concluída.")
        return result["text"]

    def summarize_text(self, text, max_tokens=1024):
        """Gera um resumo para o texto dado."""
        parts = self.text_splitter.split(text, max_tokens)
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
            self.audio_downloader.download(video_url, audio_file)
            transcription = self.transcribe_audio(audio_file)
            summaries = self.summarize_text(transcription)
            return summaries
        finally:
            if os.path.exists(audio_file):
                os.remove(audio_file)
                print(f"Arquivo temporário {audio_file} removido.")
