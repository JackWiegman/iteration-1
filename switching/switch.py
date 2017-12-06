def replace_letter(word, replaced, replacing):
	new_word = ""
	for i in range(len(word)):
		fix = word[i]
		if fix == replaced:
			fix = replacing

		new_word = new_word + fix

	return new_word

def switch_letters(word, switch_1, switch_2):
	new_word = ""
	carry_letter = "3"
	for i in range(len(word)):
		fix = word[i]
		if fix == switch_1:
			fix = carry_letter
			new_word = new_word + fix
		elif fix == switch_2:
			fix = switch_1
			new_word = new_word + fix
		else:
			new_word = new_word + fix

		final_word = ""
		for i in range(len(new_word)):
			fix = new_word[i]
			if fix == carry_letter:
				fix = switch_2
				final_word = final_word + fix
			else:
				final_word = final_word + fix
		
	return final_word

def switch_words(sentence, word1, word2):
	x = 0
	space = 0
	new_sentence = []
	sentence_words = []
	for i in range(len(sentence)):
		if sentence[i] == " ":
			sentence_words.append(sentence[:i])
			break

	for i in range(len(sentence)):
		if sentence[i] == " " or sentence[i] == ".":
			sentence_words.append(sentence[(space + 1):i])
			space = space + (i - x)
			x = len(sentence[:i])
	sentence_words.remove(sentence_words[1])

	filler = "1"
	for i in range(len(sentence_words)):
		fix = sentence_words[i]
		if fix == word1:
			fix = word2
			new_sentence.append(fix)
		elif fix == word2:
			fix = word1
			new_sentence.append(fix) 
		else:
			new_sentence.append(fix)

	final_sentence = ""
	for i in range(len(new_sentence)):
		final_sentence = final_sentence + new_sentence[i] + " "


	return final_sentence

def sentence_to_list(sentence):
	x = 0
	space = 0
	new_sentence = []
	sentence_words = []
	for i in range(len(sentence)):
		if sentence[i] == " ":
			sentence_words.append(sentence[:i])
			break

	for i in range(len(sentence)):
		if sentence[i] == " ":
			sentence_words.append(sentence[(space + 1):i])
			space = space + (i - x)
			x = len(sentence[:i])

	if len(sentence_words) >= 1:
		sentence_words.remove(sentence_words[1])
		sentence_words.append(sentence[space + 1:])

	return sentence_words

def list_to_sentence(new_sentence):
	final_sentence = ""
	for i in range(len(new_sentence)):
		final_sentence = final_sentence + new_sentence[i] + " "

	return final_sentence

def censor(sentence, bad_words, replacement_words):
	low_sen = sentence.lower()
	sentence_list = sentence_to_list(low_sen)
	new_sentence = []
	times_replaced = 0
	replacement_word = 0
	words = 0

	for i in range(len(sentence_list)):
		for k in range(len(bad_words)):
			if sentence_list[i] == bad_words[k]:
				# replacement = sentence_list[i][0] + ("*" * len(sentence_list[i][1:]))
				if i == 0:
					new_sentence.append(replacement_words[replacement_word][0].upper() + replacement_words[replacement_word][1:]) # put replacement to star it out
				else:
					new_sentence.append(replacement_words[replacement_word])

				replacement_word += 1
				replacement_word = replacement_word % len(replacement_words)
				# if replacement_word >= len(replacement_words):
				# 	replacement_word = 0


		if sentence_list[i] not in bad_words:
			if i == 0 or sentence_list[i] == 'i':
				new_sentence.append(sentence_list[i][0].upper() + sentence_list[i][1:])
			else:
				new_sentence.append(sentence_list[i])

		words += 1


	final_sentence = list_to_sentence(new_sentence)


	return final_sentence



print replace_letter("banana", "a", "!")
print switch_letters("textbook", "e", "o")
print switch_words("The quick brown fox jumps over the lazy dog", "fox", "dog")
print censor("Spanish is a goddamn piece of motherfucking shit", ['shit', 'goddamn', 'motherfucking'], ['heck', 'darn'])
# print censor("I fucking hate shit spanish.")
# print censor("Hell fucking yeaaa boisss we fucking did it i censored the shit out of myself this is the goddamn best fucking shit ever.")