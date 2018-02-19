import csv
import youtube_dl
import os

playlists = {}
extension = 'mp3'


def download(song, filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': extension,
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'songs', filename + '.%(ext)s')
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(song, download=True)
        info['ext'] = extension

        return ydl.prepare_filename(info)


def generate_playlist(list, filename):
    if list is "":
        return

    playlist_list = list.split(' ')

    for playlist_title in playlist_list:
        if playlist_title in playlists.keys():
            playlists[playlist_title].append(filename)
        else:
            playlists[playlist_title] = [filename]


with open('list.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    for row in reader:
        filename = download(row[0], row[1])
        generate_playlist(row[2], filename)

    print(playlists)
