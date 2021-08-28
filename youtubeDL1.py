from __future__ import unicode_literals
import youtube_dl


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
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': "%(title)s.%(ext)s",
    'ignoreerrors': "true",
    'audio': '[ext=m4a]/mp4',
    'verbose': True

}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    url = input("Enter channel URL:")
    #url = 'https://www.youtube.com/watch?v=NUYvbT6vTPs'
    ydl.download([url])
