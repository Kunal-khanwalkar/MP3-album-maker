from ..core.audio_splitter import AudioSplitter

class GUIController:
    def __init__(self, root):
        self.root = root
        self.audio_splitter = AudioSplitter()
        self.setup_ui()

    def setup_ui(self):
        # Setup UI components here, e.g., buttons, labels, etc.
        pass

    def split_audio(self, mp3file):
        try:
            self.audio_splitter.read(mp3file)
            # Further processing...
        except Exception as e:
            print(f"Error splitting audio: {e}")

# Page - UI information

# button_split_audio -> audioSplitter

# button_set_metadata -> songTagger