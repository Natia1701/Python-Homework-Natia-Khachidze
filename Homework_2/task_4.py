speed = int(input ("Write speed of car as kmph. I can tell you is it slow, fast, moderate or very Fast. "))

if speed <= 30 :
    print ( str(speed)+ " kmph is SLOW.")
else :
    if speed <= 60 :
        print (str(speed)+ " kmph is MODERATE.")
    elif speed > 60 and speed <= 120 :
        print(str(speed)+ " kmph is Fast.")
    else :
        print(str(speed)+ " kmph is VERY FAST")