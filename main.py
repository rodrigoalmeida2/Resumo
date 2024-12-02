from Salvar_Resumo import SaveSummaries
from Summarization import VideoSummarizer
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

if __name__ == "__main__":
    token = os.getenv('ACCESS_TOKEN')  # Token da API
    video_url = "https://youtu.be/-VgHk7UMPP4"

    summarizer = VideoSummarizer(token)
    summaries = summarizer.process_video(video_url)
    # Salvar os resumos
    SaveSummaries.save_to_pdf(summaries, output_file="resumo_video.pdf")
    SaveSummaries.save_to_word(summaries, output_file="resumo_video.docx")
