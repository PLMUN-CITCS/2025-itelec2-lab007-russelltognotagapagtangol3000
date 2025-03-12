import math  # Import the math module

# Get numerical input from the user
user_number = float(input("Enter a number to perform operations on: "))

# Perform arithmetic operations
addition = user_number + 10
subtraction = user_number - 5
multiplication = user_number * 2
division = user_number / 3

# Use math library functions with error handling
sqrt_value = math.sqrt(user_number) if user_number >= 0 else "Undefined for negative numbers"
sine_value = math.sin(math.radians(user_number))  # Convert degrees to radians

# Display the results with formatted output
print("\nArithmetic Operations:")
print(f"User number + 10 = {addition:.2f}")
print(f"User number - 5  = {subtraction:.2f}")
print(f"User number * 2  = {multiplication:.2f}")
print(f"User number / 3  = {division:.2f}")

print("\nMath Library Functions:")
print(f"Square root of {user_number:.2f} is: {sqrt_value}")
print(f"Sine of {user_number:.2f} degrees is: {sine_value:.4f}")  # Sine formatted to 4 decimal places
