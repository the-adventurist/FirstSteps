word = 'hello!.'
suffix_non_letters = ''
while not word[-1].isalpha():
    suffix_non_letters += word[-1] + suffix_non_letters
    word = word[:-1]
    print(suffix_non_letters, word)
