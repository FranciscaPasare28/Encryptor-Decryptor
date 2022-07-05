import sys

args = sys.argv
password = args[1]
inputFile = args[2]
outputFile = args[3]

passwordLen = len(password)
passwordIndex = 0

with open(outputFile, "w") as outFile:
  with open(inputFile, "rb") as inFile:
    while b := inFile.read(1):
      outFile.write(chr((int.from_bytes(b, byteorder = "big")) ^ ord(password[passwordIndex])))
      passwordIndex += 1
      passwordIndex %= passwordLen