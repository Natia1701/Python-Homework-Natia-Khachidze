number = int(input("please enter number of sequence-"))

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2)+fibonacci(i-1)
i=0
while i < number:
    i=i+1
    print(fibonacci(i-1), end=" ")