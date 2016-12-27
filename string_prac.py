name = input("Enter your name: ")
print("Hello "+name+".Enter file name to open..")
file_name = input()
file_handler = open(file_name)
print("Okay,here is the content of "+file_name+":")
for line in file_handler:
  #line = line.rstrip()
  #if '@gmail.com' in line:
   # continue
  #print(line)
  line = line.rstrip()
  print(line)
