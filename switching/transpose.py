from switch import sentence_to_list, replace_letter

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
	new_string = ""
    new_list = song.split("\n")
    for l in range(len(new_list)):
        if l % 2 == 1:
            word_list = new_list[l].split(" ")
            for i in range(len(word_list)):
                if word_list[i] in chords:
                    for j in range(len(chords)):
                        if word_list[i] == chords[j]:
                            new_string = new_string + " " + chords[j + step_up]

                elif "m7" in word_list[i]:
                    for y in range(len(chords)):
                        if chords[y] == word_list[i]:
                            new_string = new_string + chords[y + step_up] + "m7"
                elif "m" in word_list[i]:
                    for x in range(len(chords)):
                        if chords[x] == word_list[i]:
                            new_string = new_string + chords[x + step_up] + "m"
                elif "#" in word_list[i]:
                    for x in range(len(chords)):
                        if chords[x] == word_list[i]:
                            new_string = new_string + chords[x + step_up] + "#"

                else:
                    new_string = new_string +" "+ word_list[i]

            new_string += "\n"
        else:
            new_string += new_list[l] + "\n"

    print new_list
    return new_string

    # x = 0
    # test = 0
    # new_string = ""
    # add_on_num = 0
    # new_list = sentence_to_list(song)
    # print new_list
    # for i in range(len(new_list)):
    #     if new_list[i] in chords:
    #         for j in range(0, len(chords)):
    #             if new_list[i] == chords[j]:
    #                 new_string = new_string + " " + chords[j + step_up]


        # elif "m7" in new_list[i]:
        #     for y in range(0,len(chords)):
        #         if chords[y] in new_list[i]:
        #             new_string = new_string + chords[y+step_up] + "m7"

        # elif "m" in new_list[i]:
        #     for x in range(0,len(chords)):
        #         if chords[x] in new_list[i]:
        #             new_string = new_string + chords[x+step_up] + "m"

        # if new_list[i: i + 1] in add_ons:
        # 	for k in range(len(add_ons)):
        # 		if add_ons[k] == new_list[i]:
		      #       for j in range(len(chords)):
		      #           if new_list[i] == chords[j]:
		      #               new_string = new_string + " " + chords[j + (step_up)]

	

        # for j in range(len(add_ons)):
        # 	if add_ons[j] in new_list[i]:
        # 		for k in range(len(chords)):
        # 			if chords[k] in new_list[i]:
        # 				new_string = new_string + " " + chords[k + step_up] + add_ons[k]



        # if new_list[i] not in chords and new_list[i: i + 1] not in chords:
        # 	new_string = new_string +" "+ new_list[i]
        # 	test += 1



    # print test
    # print len(new_string)
    # return new_string

print transpose(song, -1)
