def access():
  user = "fumnanya"
  situ = True
  while situ:
    id = input("Enter your username(type 'q' to quit):")
    if id == 'q':
      print("Goodbye!")
      exit()
    if id == user:
      print("Access granted!\nHello,{}".format(user))
      situ = False
    else:
      print("Access denied!")
  else:
    print("What do you wish to do next?")


access()
