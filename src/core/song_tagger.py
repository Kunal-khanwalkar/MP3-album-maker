import eyed3

class SongTagger:
    def __init__(self, logger, validator):
        self.logger = logger
        self.validator = validator

    def tag_song(self, song):
        if (not self.validator.validate_song(song)):
            self.logger.warn("Missing attributes in the song object")
        try: 
            songFile = eyed3.load(song.file_path)
            songFile.tag.artist = song.artist
            songFile.tag.album = song.album
            songFile.tag.title = song.name
            songFile.tag.track_num = song.track_number
            songFile.tag.images.set(3,open(song.album_art_path,'rb').read(),'image/' + 'jpg')
            songFile.tag.save(version=eyed3.id3.ID3_V2_3)
        except:
            self.logger.warn("Failure to add tags to the song")
