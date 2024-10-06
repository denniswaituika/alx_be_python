def perform_operation(num1, num2, operation):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num1 or num2 == 0:
            print("cannot divide by zero")
        return num1 / num2
    else:
        return "Invalid operator"
    

