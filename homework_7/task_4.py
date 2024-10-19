# დავიხმარე AI, decode იქნება keyboard_mapping-ში სიმბოლოები პირიქით
keyboard_mapping = {
    'q': ['w'],
    'w': ['e'],
    'e': ['r'],
    'r': ['t'],
    't': ['y'],
    'y': ['u'],
    'u': ['i'],
    'i': ['o'],
    'o': ['p'],
    'p': ['q'],

    'a': ['s'],
    's': ['d'],
    'd': ['f'],
    'f': ['g'],
    'g': ['h'],
    'h': ['j'],
    'j': ['k'],
    'k': ['l'],
    'l': ['a'],

    'z': ['x'],
    'x': ['c'], 
    'c': ['v'], 
    'v': ['b'],
    'b': ['n'],
    'n': ['m'],
    'm': ['z']
}

def neighbor_encode(text):
    encoded = []
    for char in text:
        if char in keyboard_mapping:
    
            encoded.append(keyboard_mapping[char][0])
        else:
            encoded.append(char)
    return ''.join(encoded)

input_text =input("your word- ") 
encoded_text = neighbor_encode(input_text)
print(encoded_text) 



