word_1 = input("please write your word or sentence. -")
word_2 = input("please write your word or sentence. -")

if len(word_1) >= len(word_2):
    for i in word_1:
        for j in word_2:
            if i == j:
                print("", end='')
            
    print("yes")
else:
    print("NO")
        

