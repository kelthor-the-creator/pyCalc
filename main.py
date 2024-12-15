# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





def add():

    try:
        a = int(input("please enter first number"))
        print(a)
    except ValueError:
        print("invalid input")
    try:
        b = int(input("please enter first number"))
        print(b)
    except ValueError:
        print("invalid input")

    answer = a + b

    return answer

def subtract():

        try:
            a = int(input("please enter first number"))
            print(a)
        except ValueError:
            print("invalid input")
        try:
            b = int(input("please enter first number"))
            print(b)
        except ValueError:
            print("invalid input")

        answer = a - b
        return answer

def divide():

    try:
        a = int(input("please enter first number"))
        print(a)
    except ValueError:
        print("invalid input")
    try:
        b = int(input("please enter first number"))
        print(b)
    except ValueError:
        print("invalid input")

    answer = a / b
    return answer

def multiply():
    try:
        a = int(input("please enter first number"))
        print(a)
    except ValueError:
        print("invalid input")
    try:
        b = int(input("please enter first number"))
        print(b)
    except ValueError:
        print("invalid input")

    answer = a * b
    return answer

def operation():
   choice= input("Please enter an operation: (+, -, /, *)")

   match choice:
       case "+":
           print("By adding these numbers you get: ", add())
       case "-":
           print("By subtraction these numbers you get: ", subtract())
       case "/":
           print("By dividing these numbers you get: ", divide())
       case "*":
           print("By multiplying these numbers you get: ", multiply())












operation()






       # def calculation(num0,num1):





# See PyCharm help at https://www.jetbrains.com/help/pycharm/



#TO DO
#add user input
#convert number to a float

#Add statements for:
#additon
#subtraction
#multiplication
#division