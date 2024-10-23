# დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1. 
# პროგრამამ უნდა დააგენერიროს n ცალი წყვილი შემთხვევითი რიცხვი a,b,
# სადაც 0<a<1 და 0<b<1. Შემოიღეთ მთვლელი counter, თუ დაგენერირებული რიცხვი აკმაყოფილებს პირობას 
# math.sqrt(a ** 2 + b ** 2) <=1, counter-ის მნიშვნელობა გაზარდეთ 1-ით. ეკრანზე დაბეჭდეთ 4 * counter / n. 
# გაუშვით პროგრამა და გადაეცით შემდეგი მნიშვნელობები: 10, 100, 100000, 10000000. Რას ამჩნევთ?

from random import uniform
import math
number_of_pairs = int(input("please enter number of pairs. - "))
counter = 0
i = 0

while i < number_of_pairs :
    a = uniform(0,1)
    b = uniform(0,1)
    print("a = " +str(a)+ "b = " +str(b))

    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1
    else:
        counter = counter
    i += 1
result = 4 * counter / number_of_pairs
print (counter)
print (result)

# წყვილების რაოდენობის ზრდასთან ერთად პროგრამას ესაჭიროება მეტი დრო საბოლოო შედეგის მისაღებად

