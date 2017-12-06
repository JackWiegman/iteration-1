import sys
from switch import *

data = open("reveloution_radio_chorus_chords.txt", 'r')
lines = data.readlines()

flats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
prefer_flats = True

def transpose(chords):
	new_song = []
	notes = flats if prefer_flats else sharps

	for i in range(len(lines)):
		if i % 2 == 0:
			x = sentence_to_list(lines[i])
			new_song.append(x)
			
		else:
			y = sentence_to_list(lines[i])
			new_song.append(y)
	
	no_blanks = []
	for i in new_song:
		if (i != '' and i != '\n'):
			no_blanks.append(new_song[i])

	return new_song
			


print transpose(lines)
