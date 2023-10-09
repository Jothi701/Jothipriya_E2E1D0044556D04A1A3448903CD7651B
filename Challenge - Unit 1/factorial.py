def recursive_factorial(n):
  if n == 1:
       return n
  else:
       return n*recursive_factorial(n-1)
number = int(input("User Input : "))
if number < 0:
    print("Wrong Input")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", number, "is", recursive_factorial(number))


