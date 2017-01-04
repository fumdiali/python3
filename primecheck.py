#simple code to check if a given number is Prime
# program requires refactoring *4/jan/2017*
def check_prime(num):
  for num in range(2,num):
    prime = True
    for i in range(2, num):
      if num % i == 0:
        prime = False


      if prime:
        print(str(num)+" is Prime!")

# run main program

def main():
  print("Program checks for Prime Numbers..")
  num = input("Enter a number,find out if it's Prime: ")
  check_prime(int(num))

if __name__ == '__main__':
    main()
