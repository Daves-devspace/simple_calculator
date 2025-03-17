#user input
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
operation= input("Enter the operation (+,-,/,*): ")

#calculations
if operation == "+":
  result = num1 + num2
  print(f"{num1} + {num2} = {result}")
elif operation == "-":
  result = num1 - num2
  print(f"{num1} - {num2} = {result}")
elif operation == "*":
  result = num1 * num2
  print(f"{num1} * {num2} = {result}")
elif operation == "/":
  if num2 != 0:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
  else:
    print("Error:Number cann't be divisible by zero.")
else:
  print("Please enter a valid operation +,-,/,*.")
  
print("Enjoy the calculations")
    
  
