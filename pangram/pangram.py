def is_pangram(sentence):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    sentence_set = set(sentence.lower())

    for letter in alpha:
        if not (letter in sentence_set):
            return False
    return True

