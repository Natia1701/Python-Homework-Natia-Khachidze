number = int(input("please enter positive ihteger less than 50 - "))

for  i in range(1,number+1):
    factor_1 = 1
    print(str(i)+ "-" +str(factor_1), end=" ")
    k=1
    counter = 0
    while k <= i :
        k=k+1
        if i % k == 0 :
            counter +=1
            print(k)
            if counter == 2:
                break




