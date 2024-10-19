number = input("please enter positive number which is less than 10 000. - ")

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