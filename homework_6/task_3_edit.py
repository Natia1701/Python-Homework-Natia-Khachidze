

k = 0
while k < 3:
    number = input("please enter positive number which is les than 10 000. - ")
    if int(number) > 10000:
        print("your number is more than 10 000, please enter correct number!")
    elif int(number) < 0:
        print("your number is negative, please enter positive number!")
    else:
        number_of_digits = len(number)
        print("number of digits are ", len(number))
        sum_of_digits = 0
        i = 0
        while i < number_of_digits :
            print (number[-(i+1)], end="")
            sum_of_digits = sum_of_digits + int(number[i])
            i+=1
        print ()
        print ("sum of digits equals " +str(sum_of_digits))
        break
    k += 1
