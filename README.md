# MP3-album-maker

Don't you just hate it when you wanted an album with separate track files but you somehow received a single 45min Audio file? Fret not, your first world issue are gone thanks to this handy tool.

Just put your Audio (MP3,WAV,etc) file in the **Data**, along with that provide a timestamps .csv file containing the metadata for every track in the album.

Metadata File format `startTime,EndTime,SongName,ArtistName`

A sample .csv is present in the **Data** folder for reference. Simply enter the metadata accordingly (Order defines the track# of the album) and run the code. All the output track files would be present in the **Album** folder inside the **Data**.

When the required libraries are installed and the required files are set; simply run `$python3 code.py`, enter the prefered album name as input, and BadaBing BadaBoom your precious album goes ZOOM.


## Dependencies
The tool runs on Python3 and required **eye3D** and **pyDub** libraries to be installed. Moreover, FFmpeg library should also be installed to successfully run pyDub on MP3 Files.

EyeD3: `https://eyed3.readthedocs.io/en/latest/index.html`
PyDub: `http://pydub.com/`
FFmpeg: `http://www.ffmpeg.org/`