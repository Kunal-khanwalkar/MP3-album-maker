import glob
import csv
from .song import Song

class CSVReader:
    def __init__(self, timestamps_csv):
        timestamps_glob = glob.glob(timestamps_csv)[0]
        fileInputStream = open(timestamps_glob,'r')
        self.reader = csv.reader(fileInputStream, delimiter=',')

    def create_songs(self, albumart):
        return [Song(name=row[2], 
                    file_path='.\\' + str(row[2]) + '.mp3', 
                    artist=row[3], 
                    start_time=row[0].split(':'), 
                    end_time=row[1].split(':'), 
                    album='album',
                    album_art_path=albumart, 
                    track_number=i) for i, row in enumerate(self.reader)]