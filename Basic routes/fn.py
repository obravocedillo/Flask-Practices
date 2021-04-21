# Auxiliary functions
def average(numbers):
    average = 0
    for number in numbers:
        average += int(number) 
    average /= len(numbers)
    return average