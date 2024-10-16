#პროგრამა ითვლის 0-დან მიწოდებულ რიცხვამდე რიცხვების ჯამს
number = int(input("please enter your number- "))

sum = 0
i = 0 
while i < number:
    sum = sum + i
    i += 1
print(f"The sum from 0 to", number, "equals", sum, ".")