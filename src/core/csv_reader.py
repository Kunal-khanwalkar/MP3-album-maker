import csv
import glob
from itertools import zip_longest
from .song import Song

class CSVReader:
    def __init__(self, logger, validator):
        self.logger = logger
        self.validator = validator
        # CSVReader.prepare_song.validate = CSVReader.validate_row

    def read(self, timestamps_csv):
        try:
            timestamps_glob = glob.glob(timestamps_csv)[0]
            fileInputStream = open(timestamps_glob,'r')
            self.reader = csv.reader(fileInputStream, delimiter=',')
        except:
            self.logger.error("Failed to read the timestamps CSV file")
            exit(1)

    def create_songs(self, albumart): 
        songs = []
        for i,row in enumerate(self.reader):
            if (not self.validator.validate_row(row)): 
                self.logger.error("Error parsing song details from CSV")
                continue

            start_time, end_time, name, *optional_fields = row
            optional_data = dict(zip_longest(['artist', 'album'], optional_fields, fillvalue=''))

            songs.append(Song(name=name,
                        file_path='.\\data\\' + str(name) + '.mp3', 
                        start_time=start_time.split(':'), 
                        end_time=end_time.split(':'), 
                        album_art_path=albumart, 
                        track_number=i,
                        **optional_data))
        return songs
        
    # Future plans for re-wiring the imports with custom validator, see visitor.py
    # def validate_row():
    #     pass