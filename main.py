import sys,caeser

allowed = ('1','2')
caeserClas = caeser.caeser()

choice = input("Enter your input: \n\n1.Decrypt Caeser\n2.Encrypt Caeser\n\nInput: ")

if allowed.index(choice) == -1:
  print("ILLEGAL INPUT")
  sys.exit()
  
string = input("Enter the caeser string: ")
shift = input("\nEnter the shift number: ")
caeserClas.choose(int(choice),string, int(shift))
