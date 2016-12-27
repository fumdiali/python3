#poorly commented code(not good practice ;])
import time

name = input("Enter your name: ")
print("Hello "+name+".Enter file name to open..")
file_name = input()
try:
  file_handler = open(file_name)
except:
  print("Ooops!"+file_name+" cannot be opened!")
  exit()
print("Okay,here comes the content of "+file_name+"...")
time.sleep(5)
for line in file_handler:
  #line = line.rstrip()
  #if '@gmail.com' in line:
   # continue
  #print(line)
  line = line.rstrip()
  print(line)
