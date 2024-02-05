#Test file to test the code implemented by Sandra.S  
import morse

def testEncode():
  assert morse.encode('us') == '..- ...', "Should be ..- ..."
  assert morse.decode('..- ...') == 'us', "Should be us"

if __name__=="__main__":
  testEncode()
  print('Everything passed')
