import sys

count_numbers = int(input())

max_number = -sys.maxsize

sum_numbers = 0
for number in range(1, count_numbers + 1):
    current_number = int(input())
    sum_numbers += current_number

    if current_number > max_number:
        max_number = current_number
sum_numbers = sum_numbers - max_number
diff = abs(sum_numbers - max_number)

if max_number == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {diff}")
