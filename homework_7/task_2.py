word = input("Please enter your word! - ")

for i in word:
    if i not in "aeiou":
        print(i, end=" ")
        
