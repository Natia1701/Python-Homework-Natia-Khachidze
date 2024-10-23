word = input("please write your word(words) - ")
i = 0
while i < len(word):
    if word[i] == "e":
        print("", end="")
    else:
        print(word[i], end="")
    i += 2
