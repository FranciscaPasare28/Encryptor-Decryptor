import sys
inputFile = sys.argv[1]
outputFile = sys.argv[2]
passFile = sys.argv[3]

inp = open(inputFile, "rb")
out = open(outputFile, "rb")
pas = open(passFile, "w")

passArray = []

for i in range(30):
  x = inp.read(1)
  y = out.read(1)
  passArray.append(chr(int.from_bytes(x, "big") ^ int.from_bytes(y, "big")))

passArray = "".join(passArray)
for i in range(10, 16):
  if passArray[:i] == passArray[i:2*i]:
    pas.write(passArray[:i])
    break