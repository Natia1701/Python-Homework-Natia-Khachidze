#პროგრამამ მიიღოს n რიცხვი და დაბეჭდოს x რიცხვი სადაც 
#x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) )
#გაუშვით პროგრამა და გადაეცით შემდეგი მნიშვნელობები: 10, 100, 10000, 100000. რას ამჩნევთ?

number = int(input("please enter your number. - "))

i=1
counter = 0
sum_of_fractions = 0

while i < number + 1:
    sum_of_fractions =sum_of_fractions + (-1)**(i + 1) / (2 * i - 1)
    i += 1
    counter += 1
x =  4 * sum_of_fractions
print(str(x))
print(counter)

# რაც იზრდება შეყვანილი რიცხვის მნიშვნელობა მეტი სიზუსტით ვიღებთ pi რიცხვის მნიშვნელობას.