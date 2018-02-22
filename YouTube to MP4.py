from pytube import YouTube



def download():
    print('Enter YouTube link: ')
    link = input()
    print('Video is downloading...')
    yt = YouTube(link)
    title = yt.title
    stream = yt.streams.first()
    stream.download()
    print('Your video "{}" has finished downloading. Check your folder!'.format(title)) # add file location



download()