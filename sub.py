print("This is a program to subtract two numbers in a loop and store the difference in a list.")
n=int(input("Enter the Length of loop: "))
sum=[]
for i in range(n):
    variable1=int(input("Enter the " + str(i+1) + " Loop First Number: "))
    variable2=int(input("Enter the " + str(i+1) + " Loop Second Number: "))
    sum.append(variable1-variable2)
print("Show the List:", sum)