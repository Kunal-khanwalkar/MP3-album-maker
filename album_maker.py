from src.io.argument_parser import ArgumentParser
from src.audio_splitter import AudioSplitter
from src.csv_reader import CSVReader
from src.song_tagger import SongTagger
from src.yt_dlp_factory import YTDLPFactory

args = ArgumentParser()


yt_dlp_mp3_downloader = YTDLPFactory(opts=args.getOpts())
yt_dlp_mp3_downloader.download(args.getURL())

csv_reader = CSVReader('./data/Sample_CSV.csv')
songs = csv_reader.create_songs('./temp_album.jpg')
audioSplitter = AudioSplitter('./temp_album.mp3')
[audioSplitter.export(song.start_time, song.end_time, song.file_url) for song in songs]

songTagger = SongTagger()
for song in songs: songTagger.tag_song(song)