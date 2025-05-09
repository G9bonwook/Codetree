word = input()

leng = len(word)

word = word[:1] + 'a' + word[2:leng]
word = word[:leng -2] + 'a' + word[leng-1:]

print(word)