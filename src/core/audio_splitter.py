from pydub import AudioSegment

class AudioSplitter:
    def __init__(self, logger):
        self.logger = logger

    def read(self, audio_file):
        try: 
            self.audio_file = AudioSegment.from_file(audio_file)
        except:
            self.logger.error("Failed to read the audio file")
            exit(1)

    def export(self, song):
        self.logger.debug(f"Exporting {song.name} to {song.file_path}")
        self._split(song.start_time,song.end_time).export(song.file_path, format='mp3')

    def _split(self, start, end):
        return self.audio_file[self._convert_to_ms(start):self._convert_to_ms(end)]

    def _convert_to_ms(self, time_array):
        return (int(time_array[0]) * 60 + int(time_array[1])) * 1000