import random
colors = ["club", "daimond",  "heart", "spader"]
value = ["A", "K", "J", "Q", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
random_value = random.choice(value)
random_color = random.choice(colors)
print(random_color, random_value)
