replacements = {"I":"You","Me":"You","My":"Your","We":"You","Us":"You", "Mine":"Yours"}
def changePerson(sentence):
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word,word))
	return " ".join(replyWords)
