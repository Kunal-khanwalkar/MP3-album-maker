import os
from .io.argument_parser import ArgumentParser
from .core.audio_splitter import AudioSplitter
from .core.csv_reader import CSVReader
from .core.song_tagger import SongTagger
from .core.yt_dlp_factory import YTDLPFactory

class AlbumMaker:
    mp3file: str = './temp_album.mp3'
    albumArt: str = './temp_album.jpg'

    def __init__(self):
        self.args = ArgumentParser()
        self.yt_dlp_mp3_downloader = YTDLPFactory(opts=self.args.get_opts())
        self.csv_reader = CSVReader()
        self.audioSplitter = AudioSplitter()
        self.songTagger = SongTagger()

    def make_album(self):
        self.csv_reader.read(self.args.get_csv())
        songs = self.csv_reader.create_songs(self.albumArt)

        self.yt_dlp_mp3_downloader.download(self.args.get_url())

        self.audioSplitter.read(self.mp3file)

        [self.audioSplitter.export(song.start_time, song.end_time, song.file_path) for song in songs]

        for song in songs: self.songTagger.tag_song(song)

        self._cleanup()

    def _cleanup(self):
        os.remove(self.mp3file)
        os.remove(self.albumArt)
