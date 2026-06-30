print("This is a program to divide two numbers in a loop and store the quotient in a list.")
n=int(input("Enter the Length of loop: "))
quotient=[]
remainder=[]
for i in range(n):
    variable1=int(input("Enter the " + str(i+1) + " Loop Dividend Number: "))
    variable2=int(input("Enter the " + str(i+1) + " Loop Divisor Number: "))
    quotient.append(variable1/variable2)
    remainder.append(variable1%variable2)
print("Show the quotients:", quotient)
print("Show the remainders:", remainder)