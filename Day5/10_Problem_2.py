def returning_only_single_letter(word):
    word = list(word)
    word1 = sorted(set(word))
    print(word1)

returning_only_single_letter("entertaining")


