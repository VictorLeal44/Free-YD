import yt_dlp
import os

carpeta_musica = os.path.join("Descargas/Música")
carpeta_video = os.path.join("Descargas/Vídeos")

def nombre(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', None)
        return title
    except Exception as e:
        return e

def musica(video_url):
    try:
        ydl_opts = {
                'ffmpeg_location': 'PATH_Programs-ytdpl',
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(carpeta_musica, "%(title)s.%(ext)s"),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3', 
                }]
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except:
        pass

def video(url,formato):
    try:
        ydl_opts = {
        'ffmpeg_location': 'PATH_Programs-ytdpl',
        'format':f"bestvideo[height<={formato}][ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        'outtmpl': os.path.join(carpeta_video, "%(title)s.%(ext)s")
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url]) 
    except:
        pass