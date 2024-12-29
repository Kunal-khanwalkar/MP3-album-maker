import yt_dlp as ydl

class YTDLPFactory:
    def __init__(self, opts):
        self.ydl = ydl.YoutubeDL(self.ydl_opts(opts))

    def download(self, URL) :
        self.ydl.download([URL])

    def ydl_opts(self, opts):
        return {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'postprocessors': [{
                'key': 'FFmpegThumbnailsConvertor',
                'format': 'jpg',
                'when': 'before_dl'
            }, {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
            'outtmpl': '.\\temp_album',
            'verbose': opts
        }