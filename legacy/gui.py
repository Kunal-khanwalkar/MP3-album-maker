import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import requests
import code as cd

HEIGHT = 500
WIDTH = 600

def browsefunc(entry):
	filename = filedialog.askopenfilename()
	entry.delete(0,tk.END)
	entry.insert(0,filename)

def splice(mp3file, songTitle, startTime, endTime):
	if(mp3file=='' or songTitle=='' or startTime=='' or endTime==''):
		messagebox.showerror('ERROR','Incomplete input')
		return 

	try:
		test1 = startTime.split(':')[1]
		test2 = endTime.split(':')[1]
		test3 = mp3file.split('/')[-1].split('.')[1]		
	except:
		messagebox.showerror('ERROR','Invalid input')
		return

	audiotime = cd.Audio(mp3file,'','','.')
	audiotime.splice_song(songTitle,startTime,endTime)
	messagebox.showerror('Done','Operation successful')


def setMetadata(mp3file, songTitle, artistName, albumName, albumArt):
	if(mp3file=='' or songTitle=='' or artistName=='' or albumName=='' or albumArt==''):
		messagebox.showerror('ERROR','Incomplete input')
		return 

	audiotime = cd.Audio(mp3file,'',albumName,albumArt)
	audiotime.write_metadata(mp3file,songTitle,artistName)
	messagebox.showerror('Done','Operation successful')	



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

mp3Entry = tk.Entry(frame, font=40)
mp3Entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text="Browse Mp3", font=40, command=lambda: browsefunc(mp3Entry))
button.place(relx=0.7, relheight=1, relwidth=0.3)




lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')


startLabel = tk.Label(lower_frame, text='Start time', font=40)
startLabel.place(relx=0.025, rely=0.025, relwidth=0.25, relheight=0.1)

startEntry = tk.Entry(lower_frame, font=40)
startEntry.place(relx=0.325, rely=0.025, relwidth=0.4, relheight=0.1)

endLabel = tk.Label(lower_frame, text='End time', font=40)
endLabel.place(relx=0.025, rely=0.15, relwidth=0.25, relheight=0.1)

endEntry = tk.Entry(lower_frame, font=40)
endEntry.place(relx=0.325, rely=0.15, relwidth=0.4, relheight=0.1)

spliceButton = tk.Button(lower_frame, text="Splice", font=40, command=lambda: splice(mp3Entry.get(),songEntry.get(),startEntry.get(),endEntry.get()))
spliceButton.place(relx=0.8, rely=0.125, relwidth=0.15, relheight=0.15)

newMp3Label = tk.Label(lower_frame, text='New mp3 name', font=40)
newMp3Label.place(relx=0.025, rely=0.275, relwidth=0.25, relheight=0.1)

endEntry = tk.Entry(lower_frame, font=40)
endEntry.place(relx=0.325, rely=0.275, relwidth=0.4, relheight=0.1)



songLabel = tk.Label(lower_frame, text='Song Title', font=40)
songLabel.place(relx=0.025, rely=0.45, relwidth=0.25, relheight=0.1)

songEntry = tk.Entry(lower_frame, font=40)
songEntry.place(relx=0.325, rely=0.45, relwidth=0.4, relheight=0.1)

artistLabel = tk.Label(lower_frame, text='Artist Name', font=40)
artistLabel.place(relx=0.025, rely=0.575, relwidth=0.25, relheight=0.1)

artistEntry = tk.Entry(lower_frame, font=40)
artistEntry.place(relx=0.325, rely=0.575, relwidth=0.4, relheight=0.1)

albumLabel = tk.Label(lower_frame, text='Album Name', font=40)
albumLabel.place(relx=0.025, rely=0.7, relwidth=0.25, relheight=0.1)

albumEntry = tk.Entry(lower_frame, font=40)
albumEntry.place(relx=0.325, rely=0.7, relwidth=0.4, relheight=0.1)

albumartButton = tk.Button(lower_frame, text='Browse Art', font=40, command=lambda: browsefunc(albumartEntry))
albumartButton.place(relx=0.025, rely=0.825, relwidth=0.25, relheight=0.1)

albumartEntry = tk.Entry(lower_frame, font=40)
albumartEntry.place(relx=0.325, rely=0.825, relwidth=0.4, relheight=0.1)

editButton = tk.Button(lower_frame, text="Set\nmetadata", font=40, command=lambda: setMetadata(mp3Entry.get(), songEntry.get(), artistEntry.get(), albumEntry.get(), albumartEntry.get()))
editButton.place(relx=0.775, rely=0.6, relwidth=0.2, relheight=0.2)


exitButton = tk.Button(lower_frame, text="exit", font=40, command=lambda: exit())
exitButton.place(relx=0.9, rely=0.9, relwidth=0.1, relheight=0.1)


root.mainloop()
