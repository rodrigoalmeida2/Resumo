import os
from dotenv import load_dotenv
from Summarization import VideoSummarizer

# Carrega variáveis de ambiente
load_dotenv()

if __name__ == "__main__":
    token = os.getenv('ACCESS_TOKEN')  # Token da API
    video_url = "https://youtu.be/-VgHk7UMPP4"

    summarizer = VideoSummarizer(token)
    summaries = summarizer.process_video(video_url)
    summarizer.save_to_pdf(summaries, output_file="resumo_video.pdf")
