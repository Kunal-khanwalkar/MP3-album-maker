import re

class Validator:
    def __init__(self, logger):
        self.logger = logger

    def validate_song(self, song):
        missing_attributes = [attr for attr in ["artist", "album", "name", "track_number", "album_art_path"] 
                              if getattr(song, attr, None) is (None or '')]
        if missing_attributes:
            self.logger.debug(f"For song: {song.name}, Missing attributes: {', '.join(missing_attributes)}")
            return False
        return True

    def validate_row(self, row):
        self.logger.debug("Song details in CSV: " + str(row))

        if len(row) < 3:
            self.logger.error(f"Insufficient details for Song in row: {row}")
            return False

        timestamp_pattern = r"^(\d{1,2}:)?\d{1,2}:\d{2}$"
        if not re.match(timestamp_pattern, row[0]) or not re.match(timestamp_pattern, row[1]):
            self.logger.error(f"Invalid timestamps in row: {row}")
            return False

        return True
