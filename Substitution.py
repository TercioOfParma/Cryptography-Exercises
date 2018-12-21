substitutionTable = {
    "a": "g",
    "b": "z",
    "c": "v",
    "d": "q",
    "e": "h",
    "f": "u",
    "g": "a",
    "h": "e",
    "i": "y",
    "j": "p",
    "k": "n",
    "l": "x",
    "m": "s",
    "n": "k",
    "o": "w",
    "p": "j",
    "q": "d",
    "r": "t",
    "s": "m",
    "t": "r",
    "u": "f",
    "v": "c",
    "w": "o",
    "x": "l",
    "y": "i",
    "z": "b",
    " ": " "

}

def substitute(str):
    ciphertext = ""
    for char in str:
        tempchar = substitutionTable[char]

        ciphertext = ciphertext + tempchar

    return ciphertext


plaintext = input("Please type some plaintext")
print(substitute(plaintext.lower()))
