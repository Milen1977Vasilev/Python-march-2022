total_sum = 0
command = input()
while command != "NoMoreMoney":
    next_sum = float(command)
    if next_sum < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {next_sum:.2f}")
    total_sum += next_sum
    command = input()
print(f"Total: {total_sum:.2f}")