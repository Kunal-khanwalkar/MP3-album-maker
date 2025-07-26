import os
from .core.audio_splitter import AudioSplitter
from .core.csv_reader import CSVReader
from .core.song_tagger import SongTagger
from .core.validator import Validator
from .core.yt_dlp_factory import YTDLPFactory

class AlbumMaker:
    mp3file: str = './data/temp_album.mp3'
    albumArt: str = './data/temp_album.jpg'

    # Future plans for re-wiring the imports with custom validator, see visitor.py
    # visitor.re_wire(Song, CSVReader)
    def __init__(self, logger, args):
        self.args = args
        self.logger = logger
        self.validator = Validator(self.logger)
        self.yt_dlp_mp3_downloader = YTDLPFactory(self.logger, is_verbose=self.args.is_verbose())
        self.csv_reader = CSVReader(self.logger, self.validator)
        self.audioSplitter = AudioSplitter(self.logger)
        self.songTagger = SongTagger(self.logger, self.validator)

    def make_album(self):
        self.csv_reader.read(self.args.get_csv())
        songs = self.csv_reader.create_songs(self.albumArt)

        self.yt_dlp_mp3_downloader.download(self.args.get_url())

        self.audioSplitter.read(self.mp3file)

        self.logger.debug("Exporting the songs")
        [self.audioSplitter.export(song) for song in songs]

        self.logger.debug("Tagging the songs")
        for song in songs: self.songTagger.tag_song(song)

        self._cleanup()

    def _cleanup(self):
        try: 
            os.remove(self.mp3file)
            os.remove(self.albumArt)
        except:
            self.logger.warn("Failed to remove temporary files")
