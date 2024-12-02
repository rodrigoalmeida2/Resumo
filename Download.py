import yt_dlp

class AudioDownloader:
    """Classe responsável por baixar o áudio de um vídeo do YouTube."""
    
    @staticmethod
    def download(video_url, output_filename="audio"):
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
        print(f"Áudio baixado como {output_filename}")
        return output_filename
