import yt_dlp


def video_and_audio_download(Youtube_url,video_output,audio_output):

    ytdl_Ops = {
        'format': 'bestvideo[ext=mp4]/best',
        'outtmpl': video_output,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ytdl_Ops) as ydl:
        print('video sendo Baixado...')
        ydl.download([Youtube_url])


    ytdl_Ops = {
        'format': 'bestaudio[ext=mp3]/best',
        'outtmpl': audio_output,
        'noplaylist': True
     }


    with yt_dlp.YoutubeDL(ytdl_Ops) as ydl:
        print('Audio sendo Baixado...')
        ydl.download([Youtube_url])

    print('Download finalizado!')


youtube_url = 'https://www.youtube.com/watch?v=Rb5-5pgg9YU'
audio_output = 'john.mp3'
video_output = 'john.mp4'

video_and_audio_download(youtube_url,video_output,audio_output)