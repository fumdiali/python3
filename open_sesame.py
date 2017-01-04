print("Enter your username and password:")

username = input()
passwd = input()

if passwd.startswith("open") and passwd.endswith("sesame"):
  print("Welcome,"+username+"!")
else:
  print("Access denied")
