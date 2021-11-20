#Nested if else statement: if we have if else statement in another if else statement this is called (nesting) nested if else statement
#example:
'''In this program, we input a number
check if the number is positive or
negative or zero and display
the output'''
num = int(input("enter the number"))
if num >=0:
    if num== 0:
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")