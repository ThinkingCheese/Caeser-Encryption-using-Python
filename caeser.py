
class caeser:
  def __init__(self):
    self.abcCaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.abcLower = self.abcCaps.lower()

  def encrypt(self, string,shiftNum):
    resultString = list(string)
    length = len(self.abcCaps)
    for i, letter in enumerate(string):
      foundCaps = self.abcCaps.find(letter)
      foundLower = self.abcLower.find(letter)
      if foundCaps == -1 and foundLower == -1:
        continue
      if foundLower != -1:
        location = self.abcLower.find(letter)
        comparedLength = location + shiftNum
        if comparedLength > length:
          resultString[i] = self.abcLower[comparedLength - length]
          continue
        resultString[i] = self.abcLower[location + shiftNum]
        continue

      #otherwise
      location = self.abcCaps.find(letter)
      comparedLength = location + shiftNum
      if location + 4 > length:
        resultString[i] = self.abcLower[comparedLength - length]
        continue
      resultString[i] = self.abcCaps[location + shiftNum]
    return ''.join(resultString)

  def decrypt(self, string, shiftNum):
    resultString = list(string)
    for i, letter in enumerate(string):
      foundCaps = self.abcCaps.find(letter)
      foundLower = self.abcLower.find(letter)
      if foundCaps == -1 and foundLower == -1:
        continue
      if foundLower != -1:
        location = self.abcLower.find(letter)
        resultString[i] = self.abcLower[location - shiftNum]
        continue

      #otherwise
      location = self.abcCaps.find(letter)
      resultString[i] = self.abcCaps[location - shiftNum]
    return ''.join(resultString)

  def choose(self, result, string, shift):
    if result == 1:  #Decrypt
      print(f"\n{self.decrypt(string, shift)}")
    if result == 2:
      print(f"\n{self.encrypt(string, shift)}")
