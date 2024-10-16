
def safe_divide(numerator, denominator):
    try:
        result = float(numerator) /float(denominator)
    except ZeroDivisionError:
        return "Error Cannot divide by Zero"
    except ValueError:
        return "Kindly input numbers only"
    return f"The result of the division is {result}"
