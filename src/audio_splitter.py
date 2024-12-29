from pydub import AudioSegment

class AudioSplitter:
    def __init__(self, audio_file):
        self.audio_file = AudioSegment.from_file(audio_file)

    def export(self, start, end, output_file):
        self._split(start,end).export(output_file, format='mp3')

    def _split(self, start, end):
        return self.audio_file[self._convert_to_ms(start):self._convert_to_ms(end)]

    def _convert_to_ms(self, time_array):
        return (int(time_array[0]) * 60 + int(time_array[1])) * 1000