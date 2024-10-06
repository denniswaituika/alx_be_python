def perform_operation(num1, num2, operation):
    match operation:
        case add:
            num1 + num2
        case substact:
            num1 - num2
        case multiply:
            num1 * num2
        case division:
            if num1 or num2 == 0:
                print("Cannot divide by zero")
            else:
                num1 / num2
        case _:
            print("Input the right values")

