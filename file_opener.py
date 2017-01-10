#poorly commented code(not good practice ;])
import time

name = input("Enter your name: ")
print("Hello,{}.Enter file name to open..".format(name.capitalize()))
file_name = input()
try:
  file_handler = open(file_name)
except:
  print("Ooops!Sorry,{}! {} cannot be opened!".format(name.capitalize(),file_name))
  exit()
print("Okay,here comes the content of {}...".format(file_name))
time.sleep(5)
for line in file_handler:
  #line = line.rstrip()
  #if '@gmail.com' in line:
   # continue
  #print(line)
  line = line.rstrip()
  print(line)
time.sleep(3)
print("See you later,{}!".format(name.capitalize()))
