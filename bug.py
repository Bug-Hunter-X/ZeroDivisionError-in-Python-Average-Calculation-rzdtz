def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (will cause ZeroDivisionError):
my_list = []
average = calculate_average(my_list)