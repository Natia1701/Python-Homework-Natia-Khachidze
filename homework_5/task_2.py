for j in range(1, 10):
    for i in range(1, 10):
        product = j*i
        if i < j+1:
            print(str(i)+ "*" +str(j)+ "=" +str(product), end=" ")
        elif j==i-1:
            print()
        elif i == j+1 :
           
            print(str(i)+ "*" +str(j)+ "=" +str(product))

        

        
     