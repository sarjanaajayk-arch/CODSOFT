"THE CALCULATOR USING PYTHON PROGRAMMING LANGUAGE"
"taking the first input value"
num1 = float(input("Enter the first value : "))
if 0 <= num1 <= 10000:
    print("The value is valid")
else:
    print("The value is invalid")
    exit()
"taking the second input value"
num2 = float(input("Enter the second value : "))
if 0 <= num2 <= 10000:
    print("The value is valid")
else:
    print("The value is invalid")
    exit()
"taking the operator input"
operator  =  input("Enter the operator : ")
if operator == "+":
    print(f"the answer is {num1 + num2}")
elif operator == "-":
    print(f"the answer is {num1 - num2}")
elif operator == "*":
    print(f"the answer is {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Division by zero is not allowed")
    else:
        print(f"the answer is {num1 / num2}")
elif operator == "%":
    if num2 == 0:
        print("Modulus by zero is not allowed")
    else:
        print(f"the answer is {num1 % num2}")
else:
    print("invalid operator")