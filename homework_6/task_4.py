number = int(input("please write number below 10. - "))

i = number + 1
while i > number:
    print (i-number, end=" ")
    i+=1
    if i > 2* number:
        break
    