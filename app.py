import csv
import youtube_dl
import os

def download(song, filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'songs', filename + '.%(ext)s')
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song])

with open('songs.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    for row in reader:
        download(row[0], row[1])
