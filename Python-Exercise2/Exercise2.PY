import math


a = 5
b = 10
c = 7

a += 3


b *= 2

c %= 4


result = math.sqrt(a**2 + b**2 + c**2)


print(f"{result:.2f}")



x = int(input("Enter integer x: "))
y = int(input("Enter integer y: "))
z = int(input("Enter integer z: "))


is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50  # Or: z >= 10 and z <= 50



all_conditions_met = is_even and is_positive and is_in_range


print(f"\n--- Evaluation Results ---")
print(f"Is x ({x}) even? {is_even}")
print(f"Is y ({y}) positive? {is_positive}")
print(f"Is z ({z}) between 10 and 50? {is_in_range}")
print(f"Are all conditions met? {all_conditions_met}")

base_score = float(input("Enter your base score: "))

adjusted_score = base_score + 5 - 10


final_score = min(max(0, adjusted_score), 100)


if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Adjusted Final Score: {final_score}")
print(f"Assigned Grade: {grade}")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operation = input("Enter operation (+, -, *, /, %, **): ").strip()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            raise ZeroDivisionError("Cannot take modulo by zero.")
        result = num1 % num2
    elif operation == '**':
        result = num1 ** num2
    else:
        result = "Invalid operation selected."

    print(f"Result: {result}")

except ValueError:
    print("Error: Invalid input. Please enter valid numeric values.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


