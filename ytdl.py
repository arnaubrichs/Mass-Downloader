from __future__ import unicode_literals
import youtube_dl, os

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': input('Preferred codec (mp3, wav, aac, m4a, flac): '),
        'preferredquality': '192',
    }],
    'item_spec': input('Video selection (eg. 1,2-3,5): '),
    'max_downloads': input('Maximum downloaded files: '),
    'path': '/usr/local/Cellar/ffmpeg',
    'logger': MyLogger(),
    'file': input('Input batch file address: '), # for batch downloading, add sys and stdin
    'progress_hooks': [my_hook], # progress bar
}


# --playlist-start NUMBER              Playlist video to start at (default is
#                                      1)
# --playlist-end NUMBER                Playlist video to end at (default is
#                                      last)
# --playlist-items ITEM_SPEC           Playlist video items to download.
#                                      Specify indices of the videos in the
#                                      playlist separated by commas like: "--
#                                      playlist-items 1,2,5,8" if you want to
#                                      download videos indexed 1, 2, 5, 8 in
#                                      the playlist. You can specify range: "
#                                      --playlist-items 1-3,7,10-13", it will
#                                      download the videos at index 1, 2, 3,
#                                      7, 10, 11, 12 and 13.


def dwl_vid(): # download video function
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        os.chdir(input("Enter your download folder: ")) # download location
        ydl.download([zxt])

button = 1
while (button == int(1)):
    video_link = input("Copy & paste the URL of the YouTube video you want to download: ") # test: https://www.youtube.com/watch?v=BaW_jenozKc, https://www.bbc.co.uk/news/av/science-environment-56944931
    zxt = video_link.strip()

    dwl_vid()
    button = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))
