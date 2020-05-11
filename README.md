# MP3-album-maker

Don't you just hate it when you wanted an album with separate track files but you somehow received a single 45min Audio file? Fret not, your first world issue is gone thanks to this handy tool.

Just put your Audio (MP3,WAV,etc) file and album art (JPG,PNG) in the **Data**, along with that provide a .csv file containing the metadata for every track in the album.

Metadata File format `startTime,EndTime,SongName,ArtistName`

A sample .csv is present in the **Data** folder for reference, enter the metadata accordingly (Order defines the track# of the album).

When the required libraries are installed and the required files are set; simply run `$python3 code.py`, enter the prefered album name as input, and BadaBing BadaBoom your precious album goes ZOOM.

All the output track files will be present in the **Album** folder inside the **Data** folder.


For ease of use, a tkinter based version is also provided for the normies. You can either trim an audiofile or change it's metadata through the intuitive GUI. Simply run `$python3 gui.py`, and fill the form accordingly. I have no plans to improve this tool because tkinter is not my favourite thing to work on.


## Dependencies
The tool runs on Python3 and requires **eye3D** and **pyDub** libraries to be installed on your system. Moreover, FFmpeg library should also be installed to successfully run pyDub on MP3 Files.

EyeD3: `https://eyed3.readthedocs.io/en/latest/index.html`
PyDub: `http://pydub.com/`
FFmpeg: `http://www.ffmpeg.org/`
