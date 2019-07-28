
sen = str(input("type sentence here: "))
word = ""
words = []

def sentence_splitter(sen):

    word = ""
    words = []

    for i in range(len(sen)):
        
        if sen[i] != " ":
            word += sen[i]
        
        else:
            words.append(word)
            word = ""

    words.append(word)
    return words

words = sentence_splitter(sen)

for i in range(len(words)):

    if len(words[i]) > len(words[i - 1]):
        
        longest_word = words[i]

print("The longest word was " + longest_word + " it was " + str(len(longest_word)) + " characters long")