n = int(input())
for numbers in range(0, n + 1, 2):
    if numbers % 2 == 0:
        print(2 ** numbers)