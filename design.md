# Design / API Documentation / Whatever

## Entry Point
main.py

[TODO] default opens as a GUI tool.
With cmd line args, can be used as a CLI tool-  
`main.py <URL> <timestamps.csv>`

where URL and timestampts.csv are positional arguments.  
Example: `py main.py "https://youtu.be/restofurl" "./data/Sample_CSV.csv"`


## Core components

### Song

Song model
- name
- file_path
- artist
- start_time
- end_time
- album
- album_art_path
- track_number

### YT-DLP Factory

Dependencies: 
- [yt-dlp](https://github.com/yt-dlp/yt-dlp/tree/master) (Fork of youtube_dl)

Responsibilities:
- Creates ydl object for using yt-dlp with Python Embeddings.
- Downloads the album from the given youtube URL.
- Converts the album to mp3 codec with 256 kbps quality.
- Downloads the thumbnail from the given youtube URL.
- Converts the thumbnail to jpg for the album.

### CSV Reader

Dependencies
- glob
- csv

Responsibilities:
- Reads the timestamps.csv file to fetch song info - Artist name, album name, song duration
- Creates Song instances by reading song information from the timestamps.csv 

### Audio Splitter

Dependencies
- pydub

Responsibilities:
- Reads the mp3 file using pydub's AudioSegment.
- Splits the audio from the respective file by the given start and end time
- Outputs the audio files under `.\data\`

### Song Tagger

Dependencies
- eyed3

Responsibilties:
- Sets the metadata of an mp3 file.

## I/O

### Logger

Responsibilities:
- Provides logging functionality for all sub-components
- DEBUG statements are flagged behind `--verbose` argument
- Variadic log arguments
- Colour coded logs based on log levels

### Arguments handler

Dependencies
- argsparse

Responsibilities:
- Enables Command Line Arguments for Album Maker.
- Takes in mandatory `URL` argument which is the input album youtube url as the first positional argument.
- Takes in mandatory `CSV` argument which is the path to the timestamps.csv file as the second positional argument.
- Takes in optional `--verbose` argument for providing verbose debug output in CLI.

## [TODO] GUI

WireFrame pattern
- Reads in wireframe.xml and programatically generates widgets for the GUI.  

GUI Controller
- Binds album_maker functionalities to separate UI components

GUI functionalities:
1. Split the album completely, or just split one song
    - Enter Youtube URL
    - Take in Album as input (Drag and drop)
    - Build a CSV, song wise data entry
    - Splits the album just like CLI functionality
2. Tag a song
    - Enter details of a song (no CSV build)
    - Only updates metadata

[TODO] Batteries included

[TODO] 3.0 Wireframing driven development (Signature overrides maxxing) (WDD)

[TODO] CLI and GUI are two different ingresses
- [ ] For CLI, you can directly call each separate component or directly call the AlbumMaker
- [x] For GUI, same thing but on GUI (inherent in GUI)
- [x] Logger is global, used for both.
- [x] Argument Parser is only on the CLI ingress 