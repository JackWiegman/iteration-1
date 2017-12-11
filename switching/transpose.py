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
        if new_list[i] in chords and new_list[i] not in add_ons:
            for j in range(0, len(letters)):
                if new_list[i] == letters[j]:
                    new_string = new_string + " " + letters[j + step_up]

        elif "m7" in new_list[i]:
            for y in range(0,len(chords)):
                if chords[y] in new_list[i]:
                    new_string = new_string + chords[y+step_up] + "m7"

        elif "m" in new_list[i]:
            for x in range(0,len(chords)):
                if chords[x] in new_list[i]:
                    new_string = new_string + chords[x+step_up] + "m"
    # for i in range(len(new_list)):
    #     if new_list[i] in chords or new_list[i: i + 1] in chords:
    #     	for k in range(len(add_ons)):
    #     		if add_ons[k] not in new_list[i]:
		  #           for j in range(len(chords)):
		  #               if new_list[i] == chords[j]:
		  #                   new_string = new_string + " " + chords[j + (step_up)]
		  #       break

	

        # for j in range(len(add_ons)):
        # 	if add_ons[j] in new_list[i]:
        # 		for k in range(len(chords)):
        # 			test+=1
        # 			if chords[k] in new_list[i]:
        # 				new_string = new_string + " " + chords[k + step_up] + add_ons[k]


        # elif add_ons[x] in new_list[i]:      
        #     for k in range(len(add_ons)):
        #         if add_ons[k] in new_list[i]:
        #             for h in range(len(letters)):
        #                 if letters[h] in new_list[i]:
        #                     new_string = new_string + letters[h + step_up] + add_ons[k]
        #         break

        if new_list[i] not in chords:
            new_string = new_string +" "+ new_list[i]

    print test
    return new_string

print transpose(song, -1)
