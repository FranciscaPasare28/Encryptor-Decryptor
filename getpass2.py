import sys
import string
import itertools

outputFile = sys.argv[1]
passFile = sys.argv[2]

out = open(outputFile, "rb")
pas = open(passFile, "w")

passChars = []
passChars.extend(string.ascii_letters + string.digits)
characters = []
characters.extend(string.ascii_letters + string.digits + '''./-–=”+{}[]();:*&!?"„,"''' + " \n\t\r")

for count in range(10, 16):
  for password in itertools.product(passChars, repeat = count):
    passW = "".join(password)
    out.seek(0)
    for i in range(10000):
      char = out.read(1)
      try:
        newChar = chr(ord(passW[i % count]) ^ ord(char.decode("utf8", errors = "ignore")))
        if newChar not in characters:
          print(f"{passW} <-- NO")
          break
      except:
        newChar = ""
    else:
      print(f"{passW} <-- GOOD")
      pas.write(passW)
      exit(0)