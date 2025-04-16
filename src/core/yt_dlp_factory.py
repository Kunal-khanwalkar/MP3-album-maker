import yt_dlp as ydl

class YTDLPFactory:
    def __init__(self, logger, is_verbose):
        self.logger = logger
        self.ydl = ydl.YoutubeDL(self.ydl_opts(is_verbose))

    def download(self, URL) :
        retcode = self.ydl.download([URL])
        if retcode != 0:
            self.logger.error("Failed to download the album")
            exit(1)

    def ydl_opts(self, is_verbose):
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
            'outtmpl': '.\\data\\temp_album',
            'is_verbose': is_verbose
        }