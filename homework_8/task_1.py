string = input("please write your sentence. - ")
lowercase_string = string.lower()
print(lowercase_string)
i = 0
while i <= len(lowercase_string) // 2:

    if not lowercase_string[i].isalpha():
        if lowercase_string[i+1] == lowercase_string[-i-1]: 
            i += 1
    elif not lowercase_string[-i-1].isalpha():
        if lowercase_string[i] == lowercase_string[-i-2]:
            i += 1
    elif lowercase_string[i] == lowercase_string[-i-1]:
        i += 1
    else:
        print("your sentence is not palindrome.")
        break 
    print("your sentence is palindrome.")
    break
