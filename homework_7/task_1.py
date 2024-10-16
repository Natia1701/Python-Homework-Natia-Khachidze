word = input("please write your word(words) - ")
i = 0
while i in range(0,len(word)):
    if word[i] == "e":
        print("", end="")
    else:
        print(word[i], end="")
    i += 2
