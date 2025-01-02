import eyed3

class SongTagger:
    def __init__(self):
        pass

    def tag_song(self, song):
        songFile = eyed3.load(song.file_path)
        songFile.tag.artist = song.artist
        songFile.tag.album = song.album
        songFile.tag.title = song.name
        songFile.tag.track_num = song.track_number
        songFile.tag.images.set(3,open(song.album_art_path,'rb').read(),'image/' + 'jpg')
        songFile.tag.save(version=eyed3.id3.ID3_V2_3)
