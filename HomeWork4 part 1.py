while True:
    num1 = input("Enter first number: ")
    if num1 == "quit":
        break
    operator = input("Enter math operator :")
    if operator == "quit":
        break
    num2 = input("Enter second number :")
    if num2 == "quit":
        break
    if operator == "+":
        print(float(num1) + float(num2))
    elif operator == "/" and float(num2) == 0:
        print("you can`t divide zero")
    elif operator == "-":
        print(float(num1) - float(num2))
    elif operator == "/":
        print(float(num1) / float(num2))
    elif operator == "*":
        print(float(num1) * float(num2))
    elif operator == "/" and num2 == "0":
       print("you can`t divide zero")



