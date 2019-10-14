#Lab #4
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement:             
#
########################################

def encrypt(message, key):
    """
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'error'
        >>> encrypt('Hello',3.5)
        'error'
        >>> encrypt(5.6,3.15)
        'error'
    """
    # --- YOU CODE STARTS HERE
    if type(message) != str or type(key) != int or key < 0:
        return "error"
    l_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    u_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for x, u in enumerate(message):
        if u.isalpha() == True: 
            for y, z in enumerate(l_alphabet):
                #current issue is if the new indice is higher than 52
                if z == u: 
                    indice = y+key
                    indice = ((indice+1) % 26) -1
                    rep = l_alphabet[indice]
            for v, w in enumerate(u_alphabet):
                if w == u:
                    indice = v+key
                    indice = ((indice+1) % 26) -1
                    rep = u_alphabet[indice]
        else:
            continue
        message = message[:x] + rep + message[x+1:]
    return message

def decrypt(message, key):
    """
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'error'
        >>> decrypt('Hello',3.5)
        'error'
        >>> decrypt(5.6,3.15)
        'error'
    """
    # --- YOU CODE STARTS HERE
    if type(message) != str or type(key) != int or key < 0:
        return "error"
    l_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    u_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for x, u in enumerate(message):
        if u.isalpha() == True: 
            for y, z in enumerate(l_alphabet):
                #current issue is if the new indice is higher than 52
                if z == u: 
                    indice = y-key
                    indice = ((indice+1) % 26) -1
                    rep = l_alphabet[indice]
            for v, w in enumerate(u_alphabet):
                if w == u:
                    indice = v-key
                    indice = ((indice+1) % 26) -1
                    rep = u_alphabet[indice]
        else:
            continue
        message = message[:x] + rep + message[x+1:]
    return message