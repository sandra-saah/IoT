# Worksheet 2 part 1 
# Implemented by sandra sahnoune 21039366
# due date : 07/04/2022
# content : Morse Node for the binary tree its population, encode and decode functions

#import libraries needed to work this program as intended S.s 
from BinaryTree import BinaryTree
import asyncio
import websockets
import json

class Node:
  def __init__(self):
    self.left = None
    self.right = None
    self.char = None
  
  
  # function to populate tree
  def insertIntoTree(self, char, morse):
    for morsechar in morse:
      if morsechar == '.':
        if self.left is None:
          self.left = Node()
          self = self.left
          continue
        self = self.left
      elif morsechar == '-':
        if self.right is None:
          self.right = Node()
          self = self.right
          continue
        self = self.right
    self.char = char
  
  # function to find the populated tree for characters based on morse input
  def findChar(self, Node, char):
    leftC = '.'
    rightC = '-'
    global tempMorse
    if Node.char == char:
      return True
    if Node.left is not None and self.findChar(Node.left, char):
      tempMorse = tempMorse + leftC
      return True
    if Node.right is not None and self.findChar(Node.right, char):
      tempMorse = tempMorse + rightC
      return True
    return False

# binaryTree called and values are entered by insert function

BinaryTree = Node()
BinaryTree.insertIntoTree('E','.')
BinaryTree.insertIntoTree('T','-')
BinaryTree.insertIntoTree('I','..')
BinaryTree.insertIntoTree('A','.-')
BinaryTree.insertIntoTree('N','-.')
BinaryTree.insertIntoTree('M','--')
BinaryTree.insertIntoTree('S','...')
BinaryTree.insertIntoTree('U','..-')
BinaryTree.insertIntoTree('R','.-.')
BinaryTree.insertIntoTree('W','.--')
BinaryTree.insertIntoTree('D','-..')
BinaryTree.insertIntoTree('K','-.-')
BinaryTree.insertIntoTree('G','--.')
BinaryTree.insertIntoTree('O','---')
BinaryTree.insertIntoTree('H','....')
BinaryTree.insertIntoTree('V','...-')
BinaryTree.insertIntoTree('F','..-.')
BinaryTree.insertIntoTree('L','.-..')
BinaryTree.insertIntoTree('P','.--.')
BinaryTree.insertIntoTree('J','.---')
BinaryTree.insertIntoTree('B','-...')
BinaryTree.insertIntoTree('X','-..-')
BinaryTree.insertIntoTree('C','-.-.')
BinaryTree.insertIntoTree('Y','-.--')
BinaryTree.insertIntoTree('Z','--..')
BinaryTree.insertIntoTree('Q','--.-')
BinaryTree.insertIntoTree('5','.....')
BinaryTree.insertIntoTree('4','....-')
BinaryTree.insertIntoTree('3','...--')
BinaryTree.insertIntoTree('2','..---')
BinaryTree.insertIntoTree('+','.-.-.')
BinaryTree.insertIntoTree('1','.----')
BinaryTree.insertIntoTree('6','-....')
BinaryTree.insertIntoTree('=','-...-')
BinaryTree.insertIntoTree('/','-..-.')
BinaryTree.insertIntoTree('7','--...')
BinaryTree.insertIntoTree('8','---..')
BinaryTree.insertIntoTree('9','----.')
BinaryTree.insertIntoTree('0','-----') 
BinaryTree.insertIntoTree('.','.-.-.-') #implementing task 4 in order to support symbols
BinaryTree.insertIntoTree(',','--..--')
BinaryTree.insertIntoTree('?','..--..')
BinaryTree.insertIntoTree('!','-.-.--')
BinaryTree.insertIntoTree('’','.----.')
BinaryTree.insertIntoTree('(','-.--.')
BinaryTree.insertIntoTree(')','-.--.-')
BinaryTree.insertIntoTree('&','.-...')
BinaryTree.insertIntoTree(':','---...')
BinaryTree.insertIntoTree(';','-.-.-.')
BinaryTree.insertIntoTree('-','-....-')
BinaryTree.insertIntoTree('_','..-.-')
BinaryTree.insertIntoTree('”','.-..-.')
BinaryTree.insertIntoTree('$','...-..-')
BinaryTree.insertIntoTree('¿','..-.-')
BinaryTree.insertIntoTree('¡','--...-')


# decode function
def decode(message_de):
    message_de += ' '
    decodedMsg = ''
    current = BinaryTree
    for morse in message_de:
      for morsechar in morse:
        if morsechar == '.':
          current = current.left
        if morsechar == '-':
          current = current.right
        if morsechar == ' ':
          if current.char is not None:
            decodedMsg += current.char
          current = BinaryTree
          continue
        if morsechar == '/':
          decodedMsg += ' '
    return decodedMsg.lower()


   # returning to a lower case, make it easier for checking if x == y later


# encode function
def encode(message):
  global tempMorse
  message = message.upper() # char values in the tree are upper case, so converts the encode string to be upper case
  encodedMsg = ''
  for char in message:
    tempMorse = ''
    if char != ' ':
      if BinaryTree.findChar(BinaryTree, char):
        encodedMsg = encodedMsg + tempMorse[::-1] + ' '
    if char == ' ':
      encodedMsg += '/ '
  return encodedMsg.strip(' ')

# Worksheet 2 Part 2 
# task 2 implemented by Sandra S

#Encode ham radio message function
def encode_ham(sender,reciever,message):
    encodedMessage = reciever+"de"+sender+"="+message+"=("
    output = encode(encodedMessage)
    return output

#Decode ham radio message function
def decode_ham(decode_message):
    decode_ham = decode(decode_message)
    receiver = decode_ham.split("de")
    sender = receiver[1].split("=")
    message = (receiver[0], sender[0], sender[1])
    return message

#WS2 P2 Task 3

#Function that sends a message to the echo sever and then decodes the returned message
async def send_echo(sender,InputMessage):
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        message = json.loads(await websocket.recv())
        # Get the client_id from the join message
        if message['type'] == 'join_evt':
            client_id = message['client_id']
           #Initially the message to send is encoded into ham morse
            messageToSend = encode_ham(sender,"echo",InputMessage)
            #Then that message is sent to the echo server
            await send_message(websocket,messageToSend, client_id)
            #The returned message is then decoded and returned to the user    
            response = await recv_message(websocket)
            eng_resp = decode_ham(response)
            return(eng_resp[2])
        else:
             # If first message is not the join message exit
            print("Did not receive a correct join message")
            return 0

#This async function sends an encoded time request to the remote server and returns the returned message in a decoded and readable form.
async def send_time(sender):
    #Defining where the message should be sent to / recieved from.
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server, will send a unique id to the client.
        message = json.loads(await websocket.recv())
        #print(message)
        # Get the client_id from the join message.
        if message['type'] == 'join_evt':
            client_id = message['client_id']
            #Creates the time message to be sent over to the remote server.
            timeMessage = encode_ham(sender, "time", "hello world")
            #Sends the encoded time message to the remote server.
            await send_message(websocket, timeMessage, client_id)
            #Waits for a response from the remote server.
            response = await recv_message(websocket)
            #Decodes the encoded response from the server.
            timeDecoded = decode_ham(response)
            #print(timeDecoded)
            #Returns the decoded message recieved from the server.
            return timeDecoded
            
        else:
            # If first message is not the join message, exit.
            print("Did not recieve a correct join message")
            return 0


#Code used to send a message from the server
async def send_message(websocket, message, client_id):
        outward_message = {
        'type': 'morse_evt',
        'client_id': client_id,
        'payload': message
        }
        await websocket.send(json.dumps(outward_message))
        
#Code used to recieve a message from the server
async def recv_message(websocket):
    message = json.loads(await websocket.recv())
    return message['payload']



asyncio.run(send_time("Sandra"))
