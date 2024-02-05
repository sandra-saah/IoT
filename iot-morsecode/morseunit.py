#implementation of multiple test unit in order to check the expected results 
# implemented by Sandra S 
import unittest
import morse
import asyncio
import time
from BinaryTree import BinaryTree
import BinaryHeap
class TestMorse(unittest.TestCase):
    # Tests for the encode function in morse.py
    def test_encode_us(self):
        self.assertEqual( morse.encode('us'), '..- ...')
    def test_encode_us1(self):
        self.assertEqual( morse.encode('sandra'), '... .- -. -.. .-. .-')
    def test_encode_us2(self):
        self.assertEqual( morse.encode('Hello World'), '.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
    def test_encode_us3(self):
        self.assertEqual( morse.encode('Computer Science'), '-.-. --- -- .--. ..- - . .-. /... -.-. .. . -. -.-. .') #expect to fail
    def test_encode_us4(self):
        self.assertEqual( morse.encode('London'), '.-.. --- -. -.. --- -.') 
    def test_encode_us5(self):
        self.assertEqual( morse.encode('Algeria'), '.- .-.. --. . .-. .. .-')

    # Tests for the decode function in morse.py
    def test_decode_us(self):
        self.assertEqual(morse.decode('..- ...'), 'us')    
    def test_decode_us2(self):
        self.assertEqual(morse.decode('-... .. ... .... --- .--.'), 'rook')
    def test_decode_us3(self):
        self.assertEqual(morse.decode('.-.. --- ...- .'), 'love')
    def test_decode_us4(self):
        self.assertEqual(morse.decode('.-.. --- -. -.. --- -.'), 'Bristol')
    def test_decode_us5(self):
        self.assertEqual(morse.decode('-.-. --- -- .--. ..- - . .-. / ... -.-. .. . -. -.-. .'), 'computer science')
    def test_decode_us6(self):
        self.assertEqual(morse.decode('..-. .- .. .-.. ..-'), 'fail')

        #Tests For Binary Tree

#Tests to check if the function to test if a tree is or is not empty works
    def test_isTreeEmpty(self): 
        testTree = BinaryTree("Empty")
        self.assertEqual(testTree.isTreeEmpty(),True)

    def test_isNotEmpty(self):
        testTree = BinaryTree("Test")
        testChild = BinaryTree("TestChild")
        testTree.dot = testChild
        self.assertEqual(testTree.isTreeNotEmpty(),True)

#Function to test if a node is successfully added after te insert function is called
    def test_insert_function(self):
        testTree = BinaryTree(("B","-..."))
        BinaryTree.insert_search(testTree, "A",".-")
        self.assertEqual(testTree.dot.root,("A",".-"))

#Test for the find function (input letter and return a morse)
    def test_find_function(self):
        morseCodeLetters = [("A",".-"),("B","-..."),("C","-.-."),("D","-.."),("E","."),("F","..-."),("G","--."),("H","...."),("I",".."),("J",".---"),("K","-.-"),("L",".-.."),("M","--"),("N","-."),("O","---"),("P",".--."),("Q","--.-"),("R",".-."),("S","..."),("T","-"),("U","..-"),("V","...-"),("W",".--"),("X","-..-"),("Y","-.--"),("Z","--.."),("1",".----"),("2","..---"),("3","...--"),("4","....-"),("5","....."),("6","-...."),("7","--..."),("8","---.."),("9","----."),("0","-----"),(".",".-.-.-"), (",","--..--"),("?","..--. "), ("'",".----. "), ("!","-.-.--"), ("(","-.--."), (")","-.--.-"), ("&",".-..."), (":","---..."), (";","-.-.-."), ("+",".-.-."), ("-","-....-"), ("_","..--.-"), ('"',".-..-."), ("$","...-..-"), ("¿","..-.-"),("¡","--...-"),("/","-..-."),("+",".-.-."),("=","-...-")]
        encodeTree = None
        for lm in morseCodeLetters:
            encodeTree = BinaryTree.insert_search(encodeTree, lm[0], lm[1])
        
        self.assertEqual(encodeTree.find_search("B"),("-..."))


# Test to see if the additional symbols implemented are able to be decoded
    def test_DecodeNewSymbols(self):
        self.assertEqual(morse.decode('.-.-.- --..-- ..--.. .----. -.-.-- -.--. -.--.- .-... ---... .-.-. -....-'), ".,?’!()&:+-")
        # self.assertEqual(morse.decode('..--. -.-.-. ..--.- .-..-. ...-..- ..-.- --...-'),("?;_”$¿¡"))

# Tests to check if the additional symbols implemented are about to be encoded
    def test_FullStop(self):
        self.assertEqual(morse.encode("."), '.-.-.-')
        
    def test_Comma(self):
        self.assertEqual(morse.encode(","), '--..--')

    def test_QuestionMark(self):
        self.assertEqual(morse.encode("?"), '..--..')

    def test_Apostrophe(self):
        self.assertEqual(morse.encode("’"), '.----.')
    
    def test_ExclamationMark(self):
        self.assertEqual(morse.encode("!"), '-.-.--')
    
    def test_OpenBracket(self):
        self.assertEqual(morse.encode("("), '-.--.')

    def test_CloseBracket(self):
        self.assertEqual(morse.encode(")"), '-.--.-')

    def test_AndSymbol(self):
        self.assertEqual(morse.encode("&"), '.-...')

    def test_Colon(self):
        self.assertEqual(morse.encode(":"), '---...')

    def test_SemiColon(self):
        self.assertEqual(morse.encode(";"), '-.-.-.')

    def test_Plus(self):
        self.assertEqual(morse.encode("+"), '.-.-.')

    def test_Minus(self):
        self.assertEqual(morse.encode("-"), '-....-')

    def test_UnderScore(self):
        self.assertEqual(morse.encode("_"), '')
    
    def test_SpeechMark(self):
        self.assertEqual(morse.encode('”'), '.-..-.')

    def test_DollarSign(self):
        self.assertEqual(morse.encode("$"), '...-..-')

    def test_UpsideDownQuestionMark(self):
        self.assertEqual(morse.encode("¿"), '..-.-')

    def test_UpsideDownExclamationMark(self):
        self.assertEqual(morse.encode("¡"), '--...-')
    
    
    # Worksheet 2 Part 2
    
    # Test unit to validate the implementation of the decode_bt using Binary Heap
    def test_decode_bt1(self):
        self.assertEqual(BinaryHeap.decode_bt("--. .- -- ."),'game')
    
    def test_decode_bt2(self):
        self.assertEqual(BinaryHeap.decode_bt(".--. .-. --- --. .-. .- -- -- .. -. --."),'programming')

    def test_decode_bt3(self):
        self.assertEqual(BinaryHeap.decode_bt(".--. -.-- - .... --- -."),'python')

   #Test the encode & decode ham functions
    def test_encode_ham(self):
        self.assertEqual(morse.encode_ham("sandra","racha","hello"),".-. .- -.-. .... .- -.. . ... .- -. -.. .-. .- -...- .... . .-.. .-.. --- -...- -.--.")

    def test_decode_ham(self):
        self.assertEqual(morse.decode_ham(".-. -.. . ... -...- -.-. --- -.. .. -. --. -...- -.--."),('r','s','coding')) 
        #start from recipient - sender - message

    #Test echo & time server
    
    #Test for function that sends the morse code to the echo server
    def test_send_echo_function(self):
        self.assertEqual(asyncio.run(morse.send_echo("Sandra","Queen")),"queen")

    #Test to see if the time returned from the sever is correct
    
    def test_send_time_function(self):
        self.assertEqual(asyncio.run(morse.send_time("SendTime")),time.strftime("%H:%M:%S", time.gmtime())) 
        #print a fail during British Summer Time 


     
if __name__ == "__main__":
    unittest.main()
