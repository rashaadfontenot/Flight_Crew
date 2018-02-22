import pytube
from pytube import YouTube
import pprint


def download():
    print('Enter YouTube link: ')
    link = input()
    print('Video is downloading...')
    yt = YouTube(link)
    title = yt.title
    stream = yt.streams.first()
    stream.download()
    print('Your video {} is finished downloading. Check your folder!'.format(title))


download()