#creating calculator for addition ,subtraction,multiplication and division
#function for adding two numbers
def add(num1,num2):
    return num1+num2
#function for subtracting two numbers
def subtract(num1,num2):
    return num1-num2
#function for multiplying two numbers
def multiply(num1,num2):
    return num1*num2
#function for division of tw numbers
def divide(num1,num2):
    return num1/num2
print("please select an opertaion-\n 1:adding \n 2:subtracting \n 3:multiplication \n 4:division \n")
#taking input from the user
choice=int(input("select operations from 1,2,3,4, :"))
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if choice==1:
    print(num1+num2),add(num1,num2)
elif choice==2:
    print(num1-num2),subtract(num1,num2)
elif choice==3:
    print(num1*num2),multiply(num1,num2)
elif choice==4:
    print(num1/num2),divide(num1,num2)
else:
    print("invalid input please try again later")



