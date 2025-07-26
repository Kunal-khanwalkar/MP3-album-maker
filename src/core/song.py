class Song:
    def __init__(self, name, file_path, start_time, end_time, artist, album, album_art_path, track_number):
        self.name = name
        self.file_path = file_path
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time
        self.album = album
        self.album_art_path = album_art_path
        self.track_number = track_number

    # Future plans for re-wiring the imports with custom validator, see visitor.py
    # def validate(self):
    #     pass