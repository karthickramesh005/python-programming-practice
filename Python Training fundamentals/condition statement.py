# Conditional statemants:
#       A conditional statement tells a program to execute an action depending on whether a condition is true or false.
#     It is often represented as an if-then or if-then-else statement.The example above is a sequence of code
#   which uses a conditional statement known as an "if/then" block.


age = int(input("enter your age : "))
if age >= 18 and age <= 50:
    per = str(input("you have parant permision :  "))
    if per == "yes" :
        print("yes your eligible for ride")
    else :
        print(" sorry! your Not eligible for ride")
else:
    print("sorry! your Not eligible for ride")
