# Future plans for re-wiring the imports with custom validator, see visitor.py
# re_wire(__all__)
from src.io.argument_parser import ArgumentParser
from src.io.logger import Logger

from src.album_maker import AlbumMaker
from src.gui import GUI


args = ArgumentParser()
logger = Logger(is_verbose=args.is_verbose())

if args.get_url() and args.get_csv():
    logger.warn("CLI Ingress")
    album_maker = AlbumMaker(logger, args)
    album_maker.make_album()
else:
    logger.warn("GUI Ingress")
    wireframe_path = 'wireframe.xml'
    gui = GUI(logger)
    gui.start(wireframe_path)