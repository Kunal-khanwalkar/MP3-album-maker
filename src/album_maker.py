import os
from .io.argument_parser import ArgumentParser
from .io.logger import Logger
from .core.audio_splitter import AudioSplitter
from .core.csv_reader import CSVReader
from .core.song_tagger import SongTagger
from .core.validator import Validator
from .core.yt_dlp_factory import YTDLPFactory

class AlbumMaker:
    mp3file: str = './temp_album.mp3'
    albumArt: str = './temp_album.jpg'

    def __init__(self):
        self.args = ArgumentParser()
        self.logger = Logger(is_verbose=self.args.is_verbose())
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
