number_1 = int(input ("enter first integer please. A= "))
number_2 = int(input ("enter second integer please. B= "))

if number_1 % number_2 == 0 :
    print ("A is multiple of B if A = B*n, where n is natural  number.")
elif number_2 % number_1 == 0 :
    print ("B is multiple of A if B = A*n, where n is natural  number.")
else :
    print ("A is not multiple of B or B is not multiple of A")