number = int(input("please enter your number less than or equal 1000 - "))

while number > 1000:
    print(" please write number again.")
    number = int(input("please enter your number less than or equal 1000 - "))
 
print (str(number), end=" ")

if number % 2 == 0:
    number = number // 2
    print (str(number), end=" ")
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print (str(number), end=" ")
        else:
            number = number * 3 + 1
            print (str(number), end=" ")
else:    
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print (str(number), end=" ")
        else:
            number = number * 3 + 1
            print (str(number), end=" ")

