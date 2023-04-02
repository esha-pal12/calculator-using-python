

num1=input("enter the first number")
num2=input("enter the second number")
operation=input("insert the operation(+, -, /, *)")

add=int(num1)+int(num2)
subtract=int(num1)-int(num2)
divide=int(num1)/int(num2)
multiply=int(num1)*int(num2)

if operation=="+":
    print(add)
elif operation=="-":
    print(subtract)
elif operation=="/":
    print(divide)
elif operation=="*":
    print(multiply)
else:
    print(invalid)
