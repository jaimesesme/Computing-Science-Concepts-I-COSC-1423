#---------------------------------------------------------------
# createDecode()
# Creates a Ceasar cipher decode dictionary and returns the dictionary
#---------------------------------------------------------------
def createDecode() :

    decodeDict = {}
    
    decodeDict["d"] = "a"
    decodeDict["e"] = "b"
    decodeDict["f"] = "c"
    decodeDict["g"] = "d"
    decodeDict["h"] = "e"
    decodeDict["i"] = "f"
    decodeDict["j"] = "g"
    decodeDict["k"] = "h"
    decodeDict["l"] = "i"
    decodeDict["m"] = "j"
    decodeDict["n"] = "k"
    decodeDict["o"] = "l"
    decodeDict["p"] = "m" 
    decodeDict["q"] = "n"
    decodeDict["r"] = "o"
    decodeDict["s"] = "p"
    decodeDict["t"] = "q"
    decodeDict["u"] = "r"
    decodeDict["v"] = "s"
    decodeDict["w"] = "t"
    decodeDict["x"] = "u"
    decodeDict["y"] = "v"
    decodeDict["z"] = "w"
    decodeDict["a"] = "x"
    decodeDict["b"] = "y"
    decodeDict["c"] = "z"
    decodeDict[" "] = " "
    
    return decodeDict


#---------------------------------------------------------------
# createEncode()
# Creates a Ceasar cipher encode dictionary and returns the dictionary
#---------------------------------------------------------------
def createEncode():

    encodeDict = {}
    
    encodeDict["a"] = "d"
    encodeDict["b"] = "e"
    encodeDict["c"] = "f"
    encodeDict["d"] = "g"
    encodeDict["e"] = "h"
    encodeDict["f"] = "i"
    encodeDict["g"] = "j"
    encodeDict["h"] = "k"
    encodeDict["i"] = "l"
    encodeDict["j"] = "m"
    encodeDict["k"] = "n"
    encodeDict["l"] = "o"
    encodeDict["m"] = "p"
    encodeDict["n"] = "q"
    encodeDict["o"] = "r"
    encodeDict["p"] = "s"
    encodeDict["q"] = "t"
    encodeDict["r"] = "u"
    encodeDict["s"] = "v"
    encodeDict["t"] = "w"
    encodeDict["u"] = "x"
    encodeDict["v"] = "y"
    encodeDict["w"] = "z"
    encodeDict["x"] = "a"
    encodeDict["y"] = "b"
    encodeDict["z"] = "c"
    encodeDict[" "] = " "
    
    return encodeDict

def encryptText(message):
    word = ""
    enc_dict = createEncode()
    for letter in message:
        word += enc_dict[letter]
    return word

def decryptText(message):
    word = ""
    enc_dict = createDecode()
    for letter in message:
        word += enc_dict[letter]
    return word

def main():
    option = 4
    while option != 3:
        print(""" 
                MENU
                1. Encrypt a message
                2. Decrypt a message
                3. Quit""")
        option = int(input("\n\t\tEnter you option: "))
        if option == 1:
            print("\nENCRYPT MESSAGE")
            message = input("\t\tEnter message to Encrypt")
            print("\t\tYour message is: ",encryptText(message))
        
        if option == 2:
            print("\nDECRYPT MESSAGE")
            message = input("\t\tEnter message to Decrypt")
            print("\t\tYour message is: ",decryptText(message))
        print(""" 
                MENU
                1. Encrypt a message
                2. Decrypt a message
                3. Quit""")
        option = int(input("\n\t\tEnter you option: "))
        
main()
