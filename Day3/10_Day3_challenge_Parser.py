sentence = input("Enter a sentence: ")

list1 = []
word1 = input("Enter  words 1:")
word2 = input("Enter  words 2:")
word3 = input("Enter  words 3:")

list1.append(word1)
list1.append(word2)
list1.append(word3)

# how many times did the given words appears in the sentence.
appears1 = sentence.count(list1[0].lower())
appears2 = sentence.count(list1[1].lower())
appears3 = sentence.count(list1[2].lower())

print(f"The word \"{word1}\" appears {appears1} times")
print(f"The word \"{word2}\" appears {appears2} times")
print(f"The word \"{word3}\" appears {appears3} times")

# How many words in the sentence.
word_count = sentence.split(" ")
print(f"There are \"{len(word_count)}\" words in the sentence")

#First and last letter..
first_letter = word_count[0]
last_letter = word_count[-1]
print(f"The first letter is \"{first_letter}\" and the last letter is \"{last_letter}\"")

#inverting the word
word_count.reverse()
invert = " ".join(word_count)
print(f"We we invert the sentence it will be \"{invert}\"")


# boolean
is_python = 'python' in sentence
dic = {True: "was", False: "was not"}
print(f'The word Python {dic[is_python]} in the sentence')





