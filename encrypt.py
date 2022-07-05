import sys

args = sys.argv
password = args[1]
inputFile = args[2]
outputFile = args[3]

passwordLen = len(password)
passwordIndex = 0

with open(outputFile, "wb") as outFile:
  with open(inputFile) as inFile:
    while char := inFile.read(1):
      outFile.write((ord(char) ^ ord(password[passwordIndex])).to_bytes(1, byteorder="big"))
      passwordIndex += 1
      passwordIndex %= passwordLen