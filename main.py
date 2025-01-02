from src.album_maker import AlbumMaker

class GUI:
    def __init__(self):
        self.album_maker = AlbumMaker()


gui = GUI()
gui.album_maker.make_album()