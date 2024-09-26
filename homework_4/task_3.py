number = int(input("please enter positive number "))

if number > 0:
    for n in range (1, 1000):
        if number % n == 0 :
           print(str(n), end=" ")

else :
    print("please enter positive number.")
       