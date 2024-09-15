number = int(input ("Enter positive whole number less than 11 please! "))
prime_number_1 = 2
prime_number_2 = 3
prime_number_3 = 5
prime_number_4 = 7

remainder_1 = number % prime_number_1
remainder_2 = number % prime_number_2
remainder_3 = number % prime_number_3
remainder_4 = number % prime_number_4

                                                                                                     # martivi gamyofi aris 2, 3, 5 an 7.
if remainder_1 == 0 :
    if remainder_2 == 0 :
        print ("prime factors of the number are " +str(prime_number_1), str(prime_number_2)+ ".")     #martivi gamyofi 2 da 3-ia
    elif remainder_3 == 0 :
        print ("prime factors of the number are " +str(prime_number_1), str(prime_number_3)+ ".")     #martivi gamyofi 2 da 5-ia
    else :
       print ("prime factor of the number is only  " +str(prime_number_1)+ ".")                       #martivi gamyofi mxolod 2-ia

elif remainder_2 == 0 and remainder_1 != 0 :
    print ("prime factor of the number is only " +str(prime_number_2)+ ".")                           #martivi gamyofi mxolod 3-ia

elif remainder_3 == 0 and remainder_1 != 0 :
    print("prime factor of the number is only " +str(prime_number_3)+ ".")                            #martivi gamyofi mxolod 5-ia

elif remainder_4 == 0 :
    print ("prime factor of the number is " +str(prime_number_4)+ ".")                                #martivi gamyofi mxolod 7-ia

else :
    print ("The number does not have prime factor.")                                                  # ar aqvs martivi gamyofebi (erTianis SemTxveva)