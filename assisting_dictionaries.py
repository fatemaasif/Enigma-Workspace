import pygame

letterkeydict = {
    "A": (140, 566),
    "B": (471, 640),
    "C": (319, 639),
    "D": (294, 567),
    "E": (268, 495),
    "F": (371, 567),
    "G": (448, 567),
    "H": (523, 567),
    "I": (650, 496),
    "J": (598, 567),
    "K": (674, 567),
    "L": (699, 641),
    "M": (624, 641),
    "N": (547, 640),
    "O": (725, 497),
    "P": ( 92, 639),
    "Q": (115, 494),
    "R": (345, 495),
    "S": (217, 566),
    "T": (420, 496),
    "U": (574, 496),
    "V": (395, 639),
    "W": (192, 494),
    "X": (242, 639),
    "Y": (168, 639),
    "Z": (497, 496)}

lampdict = {
    "A": (144, 332),
    "B": (472, 403),
    "C": (321, 402),
    "D": (296, 333),
    "E": (272, 265),
    "F": (372, 333),
    "G": (448, 334),
    "H": (524, 334),
    "I": (650, 266),
    "J": (600, 335),
    "K": (676, 335),
    "L": (700, 403),
    "M": (624, 403),
    "N": (549, 403),
    "O": (725, 267),
    "P": ( 94, 401),
    "Q": (121, 264),
    "R": (347, 265),
    "S": (220, 332),
    "T": (423, 265),
    "U": (574, 266),
    "V": (397, 402),
    "W": (197, 264),
    "X": (246, 402),
    "Y": (170, 401),
    "Z": (499, 265)}

#when signal goes back through the rotor, the translation has to happen backwards, so this function gives a dictionary for each rotor's inverse mapping. 
def invertKey(noniverted_dict):
    inverteddict = {v: k for k, v in noniverted_dict.items()} #exchange the keys and values i.e. the letters translated from and letters translated to
    converttoOrderedList = sorted(inverteddict.items()) #sort the list of new values according to ascending order (from A to Z) 
    dictionary = dict(converttoOrderedList)
    return dictionary


RotorI = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G", "G": "D", "H": "Q", "I": "V", "J": "Z", "K": "N", "L": "T", "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U", "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R", "Y": "C", "Z": "J"}

RotorI_bw = invertKey(RotorI)

RotorII = {"A": "A", "B": "J", "C": "D", "D": "K", "E": "S", "F": "I", "G": "R", "H": "U", "I": "X", "J": "B", "K": "L", "L": "H", "M": "W", "N": "T", "O": "M", "P": "C", "Q": "Q", "R": "G", "S": "Z", "T": "N", "U": "P", "V": "Y", "W": "F", "X": "V", "Y": "O",
"Z": "E"}

RotorII_bw = invertKey(RotorII)

RotorIII = {"A": "B", "B": "D", "C": "F", "D": "H", "E": "J", "F": "L", "G": "C", "H": "P", "I": "R", "J": "T", "K": "X", "L": "V", "M": "Z", "N": "N", "O": "Y", "P": "E", "Q": "I", "R": "W", "S": "G", "T": "A", "U": "K", "V": "M", "W": "U", "X": "S", "Y": "Q", "Z": "O"}

RotorIII_bw = invertKey(RotorIII)

RotorIV = {"A": "E", "B": "S", "C": "O", "D": "V", "E": "P", "F": "Z", "G": "J", "H": "A", "I": "Y", "J": "Q", "K": "U", "L": "I", "M": "R", "N": "H", "O": "X", "P": "L", "Q": "N", "R": "F", "S": "T", "T": "G", "U": "K", "V": "D", "W": "C", "X": "M", "Y": "W", "Z": "B"}

RotorIV_bw = invertKey(RotorIV)

RotorV = {"A": "V", "B": "Z", "C": "B", "D": "R", "E": "G", "F": "I", "G": "T", "H": "Y", "I": "U", "J": "P", "K": "S", "L": "D", "M": "N", "N": "H", "O": "L", "P": "X", "Q": "A", "R": "W", "S": "M", "T": "J", "U": "Q", "V": "O", "W": "F", "X": "E", "Y": "C", "Z": "K"}

RotorV_bw = invertKey(RotorV)

Reflector = {"A": "I", "B": "X", "C": "U", "D": "H", "E": "F", "F": "E", "G": "Z", "H": "D", "I": "A", "J": "O", "K": "M", "L": "T", "M": "K", "N": "Q", "O": "J", "P": "W", "Q": "N", "R": "S", "S": "R", "T": "L", "U": "C", "V": "Y", "W": "P", "X": "B", "Y": "V", "Z": "G"}

w = 32
h = 63
steckerbrettdict = {
    'Q': pygame.Rect((31, 380),(w,h)),
    'W': pygame.Rect((120, 380),(w,h)),
    'E': pygame.Rect((210, 380),(w,h)),
    'R': pygame.Rect((298, 380),(w,h)),
    'T': pygame.Rect((386, 380),(w,h)),
    'Z': pygame.Rect((474, 380),(w,h)),
    'U': pygame.Rect((564, 380),(w,h)),
    'I': pygame.Rect((652, 380),(w,h)),
    'O': pygame.Rect((742, 380),(w,h)),
    #--------line 1 end--------
    'A': pygame.Rect((73, 480),(w,h)),
    'S': pygame.Rect((163, 480),(w,h)),
    'D': pygame.Rect((251, 480),(w,h)),
    'F': pygame.Rect((341, 480),(w,h)),
    'G': pygame.Rect((429, 480),(w,h)),
    'H': pygame.Rect((517, 480),(w,h)),
    'J': pygame.Rect((606, 480),(w,h)),
    'K': pygame.Rect((694, 480),(w,h)),
    #--------line 2 end--------
    'P': pygame.Rect((31, 580),(w,h)),
    'Y': pygame.Rect((121, 580),(w,h)), 
    'X': pygame.Rect((210, 580),(w,h)), 
    'C': pygame.Rect((299, 580),(w,h)),
    'V': pygame.Rect((388, 580),(w,h)),  
    'B': pygame.Rect((478, 580),(w,h)), 
    'N': pygame.Rect((567, 580),(w,h)),      
    'M': pygame.Rect((656, 580),(w,h)), 
    'L': pygame.Rect((744, 580),(w,h))}
