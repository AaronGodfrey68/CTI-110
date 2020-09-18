# Ask user to enter the first number, assign it a proper name
#4. Ask user to enter the second number, assign it a proper name
#5. Add the two numbers
#6.Multiply the two numbers
#7. Display the following:
   #*First Number Entered
   #*Second Number Entered
   #*Sum of both numbers
  # *Result of Multiplying the two numbers
#Aaron Godfrey
#Date: 09/16
#CTI-110 P1HW2-Basic MAth

print('Welcome to my first', end= ' ')
print('Program')
user_num1 = int(input("please Enter first number:", ))
user_num2 = int(input("please Enter second number:", ))

print("First number entered:", user_num1)
print("Second number entered:", user_num2)
print("would you like to see quick Math?")#<sorry about this just a little fun part for myself
input()
print('The sum of both numbers is:', user_num1 + user_num2)

print("The Result of Multiplying both numbers:", user_num1*user_num2)
print('Have a Good day')
