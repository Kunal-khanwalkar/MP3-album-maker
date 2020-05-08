import glob
import eyed3
from pydub import AudioSegment
import csv

class Audio:	

	mp3file = None
	datafile = None
	albumName = None

	def __init__(self,inputmp3,datafile,albumName):
		self.mp3file = AudioSegment.from_mp3(inputmp3)		
		self.datafile = datafile
		self.albumName = albumName

	def Make_album(self):
		fileInputStream = open(self.datafile,'r')
		reader = csv.reader(fileInputStream,delimiter=',')

		i=0
		for row in reader:
			
			i+=1
			startMin = int(row[0].split(':')[0])
			startSec = int(row[0].split(':')[1])
			endMin = int(row[1].split(':')[0])
			endSec = int(row[1].split(':')[1])
			#print(str(startMin) + ":" + str(startSec) + ", " + str(endMin) + ":" + str(endSec))

			startTime = (startMin*60 + startSec)*1000			
			endTime = (endMin*60 + endSec)*1000			

			songName = row[2]
			songFileString = '.\\data\\Album\\' + songName + '.mp3'
			artist = row[3]			

			extract = self.mp3file[startTime:endTime]
			extract.export(songFileString, format='mp3')

			songFile = eyed3.load(songFileString)			
			songFile.tag.artist = artist
			songFile.tag.album = self.albumName			
			songFile.tag.title = songName
			songFile.tag.track_num = i
			songFile.tag.save()

			print('Song: "' + songName + '" done')


if __name__=='__main__':

	inputmp3 = glob.glob('.\\data\\*.mp3')[0]	
	datafile = glob.glob('.\\data\\*.txt')[0]	

	albumName = str(input('Enter album name: '))
	
	audiotime = Audio(inputmp3,datafile,albumName)
	audiotime.Make_album()