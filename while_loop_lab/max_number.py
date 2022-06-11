import sys
command = input()
max_number = - sys.maxsize
while command != "Stop":
    next_number = int(command)
    if next_number > max_number:
        max_number = next_number
    command = input()
print(max_number)