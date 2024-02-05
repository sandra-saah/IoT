# Test the morse code I/O implemented by sandra S
import morse
import asyncio
from BinaryHeap import decode_bt

if __name__ == "__main__":
    e = morse.encode('us')
    print('%s' % e)
    d = morse.decode(e)
    print('%s' % d)
    assert morse.encode('us') == '..- ...', "Should be ..- ..."
    assert morse.decode('..- ...') == 'us', "Should be us"
    
    #Test the decode_bt binary Heap WS2 P2 task 1
    test = decode_bt('... .- -. -.. .-. .-') #should print sandra
    print(test)
    
    # Test the encode & decode ham
    print(morse.encode_ham("Sender","Reciever","Message"))
    print(morse.decode_ham(".-. .---- -.. . ... .---- -...- .... .. -...- -.--.")) #must print a tuple
    
    # Test the echo / time functions 
    print(asyncio.run(morse.send_echo("sandra","Testing")))
    print(asyncio.run(morse.send_time("sandra")))

