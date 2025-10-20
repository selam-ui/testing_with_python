# first we have to input 2 numbers
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
# next we input operations
op = input("enter opration (+,-,*,/):")
#in the next step we calculate
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 == 0:
        result ="error: division by zero!"
    else:
        result = num2 / num1
else:
    result = "invalid operation!"
print("result:", result)


