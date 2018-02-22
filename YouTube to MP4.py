import pytube
from pytube import YouTube
import pprint


def download():
    print('Enter YouTube link: https://www.youtube.com/watch?v=cTtILc5SS98')
    link = 'https://www.youtube.com/watch?v=cTtILc5SS98'
    yt = YouTube(link)
    #pprint.pprint(yt.streams.filter(progressive=True).all())
    title = yt.title
    stream =  yt.streams.first()
    stream.download()
    print('Your video {} is downloaded!'.format(title))


download()