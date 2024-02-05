# Worksheet 2 part 2 implemented by Sandra S
# Implementation of the decode_bt function using a binary heap by Sandra S.

def decode_bt(msg_dec):
    letters = ["Root","E","T","I","A","N","M","S","U","R","W","D","K","G","O","H","V","F","*","L","*","P","J","B","X","C","Y","Z","Q","*","*","5","4","*","3","*","*","*","2","*","*","+","*","*","*","*","1","6","=","/","*","*","*","*","*","7","*","*","*","8","*","9","0"]   
    
    decodedMessage = ""
    targetMorse = msg_dec.split(" ")
    for eachLetter in targetMorse:
        i = 1
        for eachDotDash in eachLetter:
            
            if eachDotDash == ".":
                i = (2*i) #left

            if eachDotDash == "-":
                i = (2*i)+1 #right

        decodedMessage += letters[i-1]
    return decodedMessage.lower()


