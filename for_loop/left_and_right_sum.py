count_of_numbers = int(input())
left_sum = 0
right_sum = 0
for numbers in range(2 * count_of_numbers):
    number = int(input())
    if count_of_numbers > numbers:
        left_sum += number
    else:
        right_sum += number
if left_sum == right_sum:
    print(f" Yes, sum = {right_sum}")
else:
    print(f" No, diff = {abs(left_sum - right_sum)}")

