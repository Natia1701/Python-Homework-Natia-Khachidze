word = input("please enter your word.- ")
print(len(word))


if len(word) % 2 == 0:
    print (word [len(word)//2-1], word[len(word)//2])
else:
    i=0
    while i < 5:
        print(word[-1],word[0], word[len(word)//2])
        i += 1
