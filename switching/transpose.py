# import sys
# from switch import *

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

from switch import sentence_to_list

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

chords = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F","Gb", "G", "Ab"]
letters = ["A", "B", "C", "D", "E", "F", "G"]
add_ons = ["m7", "m", "add7", "add9"]
def transpose(song, step_up):
    x = 0
    test = 0
    new_string = ""
    add_on_num = 0
    new_list = sentence_to_list(song)
    print new_list
    for i in range(len(new_list)):
        if new_list[i] in chords:
            for j in range(len(chords)):
                if new_list[i] == chords[j]:
                    new_string = new_string + " " + chords[j + (step_up)]

        elif add_ons[x] in new_list[i]:   
            test += 1      
            for k in range(len(add_ons)):
                if add_ons[k] in new_list[i]:
                    for h in range(len(letters)):
                        if letters[h] in new_list[i]:
                            new_string = new_string + letters[h + step_up] + add_ons[k]
                break

        else:
            new_string = new_string +" "+ new_list[i]

    return new_string

print transpose(song, -1)
