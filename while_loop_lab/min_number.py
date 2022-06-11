import sys

min_number = sys.maxsize
number = input()
while number != "Stop":
    next_number = int(number)
    if next_number < min_number:
        min_number = next_number
    number = input()
print(min_number)