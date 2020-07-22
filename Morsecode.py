class Morse():
    def __init__(self):
        global DICT
        DICT = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 
                'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 
                'l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-', 
                'r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--', 
                'x':'-..-', 'y':'-.--', 'z':'--..','1':'.----', '2':'..---',
                '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...',
                '8':'---..', '9':'----.','0':'-----',', ':'--..--','.':'.-.-.-',
             '?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
    def encode(self,message): 
        cipher = '' 
        for m in message: 
            if m != ' ': 
                cipher += DICT[m] + ' '
            else: 
                cipher += ' '
        return cipher 

    def decode(self,message): 
        message += ' '
        decrypt = '' 
        character = '' 
        for m in message: 
            if m!= ' ': 
                spaces = 0
                character += m
            else: 
                spaces += 1
                if spaces == 2 : 
                    decrypt += ' '
                else:  
                    decrypt += list(DICT.keys())[list(DICT.values()).index(character)] 
                    character = '' 
        return decrypt
