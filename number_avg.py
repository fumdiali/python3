#no error checking
#does not validate user input
#memory intensive,if user inputs millions of numbers
name = input("Enter a user name:")
print("*****************")
print(" Welcome,"+name)
print("*****************")
print("Give me some numbers,I will tell you their average..")
print("Enter '0' when all are in.")

numlist = list()

while True:
  user_input = input("Enter a number: ")
  if user_input == '0':
    break
  value = float(user_input)
  numlist.append(value)

#sum() and len() adds the entries and counts them for us,respectively
avg = sum(numlist)/len(numlist)

print("The average of your "+str(len(numlist))+"  numbers is "+str(avg))
