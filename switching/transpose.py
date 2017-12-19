song = """
G  Em  G  Em  G  Em  A   Em A G  2x

C                        D
So, so you think you can tell 
            Am
Heaven from Hell, 
                G
Blue skies from pain. 
                     D
Can you tell a green field 
                  C
From a cold steel rail? 
               Am
A smile from a veil? 
                     G
Do you think you can tell? 
                        C
And did they get you to trade 
                D
Your heroes for ghosts? 
              Am
Hot ashes for trees? 
              G
Hot air for a cool breeze? 
                 D
Cold comfort for change? 
              C
And did you exchange 
                      Am
A walk on part in the war 
                     G
For a lead role in a cage? 
G  Em  G  Em  G  Em  A  Em A   G  

C                               D
How I wish, how I wish you were here. 
           Am
We're just two lost souls 

Swimming in a fish bowl, 
G
Year after year, 
D                     
Running over the same old ground. 
             C
What have we found? 
             Am
The same old fears. 
              G
Wish you were here.
G  Em  G  Em  G  Em  A  Em A G  4x"""
 
chords = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F","Gb", "G", "Ab"]
letters = ["A", "B", "C", "D", "E", "F", "G"]
def transpose(song, step_up):
    new_string = ""
    lines = song.split("\n")
    for l in range(len(lines)):
        word_list = lines[l].split(" ")
        for i in range(0,len(word_list)):
            if len(word_list[i]) <= 3:
                boolean = True
            else:
                boolean = False
                break

        if boolean == True:
            for i in range(len(word_list)):
                    if word_list[i] in chords:
                        for j in range(len(chords)):
                            if word_list[i] == chords[j]:
                                new_string = new_string + " " + chords[j + step_up]

                    elif "m7" in word_list[i]:
                        for y in range(len(letters)):
                            if letters[y] in lines[i]:
                                new_string = new_string + chords[y + step_up] + "m7"

                    elif "m" in word_list[i]:
                        for x in range(len(letters)):
                            if letters[x] in word_list[i]:
                                new_string = new_string + chords[x + step_up] + "m"

                    elif "#" in word_list[i]:
                        for x in range(len(letters)):
                            if letters[x] in word_list[i]:
                                new_string = new_string + chords[x + step_up] + "#"

                    else:
                        new_string = new_string +" "+ word_list[i]
            new_string += "\n"
        else:
            new_string += lines[l] + "\n"
    return new_string

print transpose(song, 1)
