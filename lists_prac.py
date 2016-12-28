name = input("Enter a user name:")
print("*****************")
print(" Welcome,"+name)
print("*****************")
print("Give me some numbers,I will tell you their average..")
print("Enter 'done' when all are in.")

numlist = list()

while True:
  user_input = input("Enter a number: ")
  if user_input == 'done':
    break
  value = float(user_input)
  numlist.append(value)

avg = sum(numlist)/len(numlist)

print("The average of your "+str(len(numlist))+"  numbers is "+str(avg))
