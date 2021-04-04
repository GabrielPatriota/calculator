import input

if input.inputSign == "+":
    print("Let's do some sum\n")
    x = input.inputOne + input.inputTwo
    print("Sum is: " + str(x))

if input.inputSign == "x" or input.inputSign == "*":
    print("Let's do some multiplication")
    x = input.inputOne * input.inputTwo
    print("Multiplication is: " + str(x))

if input.inputSign == "-":
    print("Let's do some subtraction")
    x = input.inputOne - input.inputTwo
    print("Subtraction is: " + str(x))

if input.inputSign == "/":
    print("Let's do some division")
    x = input.inputOne / input.inputTwo
    print("Division is: " + str(x))