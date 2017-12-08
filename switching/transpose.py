import sys
from switch import *

# data = open("reveloution_radio_chorus_chords.txt", 'r')
# lines = data.readlines()

# flats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
# notes_sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
# add_ons = ['m', 'm7']

# def transpose(notes_sharps):
# 	new_song = []

# 	for i in range(len(lines)):
# 		if i % 2 == 0:
# 			x = sentence_to_list(lines[i])
# 			new_song.append(x)
			
# 		else:
# 			y = sentence_to_list(lines[i])
# 			new_song.append(y)
	
# 	# Make everything into one list
# 	one_list = []
# 	for i in range(len(new_song)):
# 		for k in range(len(new_song[i])):
# 			one_list.append(new_song[i][k])


# 	# Make list of just notes
# 	notes = []
# 	for i in range(len(one_list)):
# 		for k in range(len(notes_sharps)):
# 			if one_list[i] == notes_sharps[k]:
# 				notes.append(notes_sharps[k])
# 			for h in range(len(add_ons)):
# 				if one_list[i] == notes_sharps[k] + add_ons[h]:
# 					notes.append(notes_sharps[k] + add_ons[h])
# 				return notes

# 	return notes
			


# print transpose(lines)

song = """
 C          Am7
There's a feeling I get,
           Am
When I look to the West.
            C           G               Am
And my spirit is crying for leaving.
            C                   Am7
In my thoughts I have seen,
                Am
Rings of smoke through the trees,
                C         G                     Am
And the voices of those who stand looking."""

Chords = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F","Gb", "G", "Ab"]
Letters = ["A", "B", "C", "D", "E", "F", "G"]
def transpose(song,step_down):
    new_string = ""
    new_list = split_words(song)
    print new_list
    for i in range(0,len(new_list)):
        if new_list[i] in Chords:
            for j in range(0, len(Chords)):
                if new_list[i] == Chords[j]:
                    new_string = new_string + " " + Chords[j-step_down]
        elif "m7" in new_list[i]:
            for y in range(0,len(Letters)):
                if Letters[y] in new_list[i]:
                    new_string = new_string + Letters[y-step_down] + "m7"
        elif "m" in new_list[i]:
            for x in range(0,len(Letters)):
                if Letters[x] in new_list[i]:
                    new_string = new_string + Letters[x-step_down] + "m"
        else:
            new_string = new_string +" "+ new_list[i]
    return new_string

print transpose(song, 1)