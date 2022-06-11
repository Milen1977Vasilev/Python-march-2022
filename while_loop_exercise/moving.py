lenght = int(input())
weight = int(input())
hight = int(input())
total_place = lenght * weight * hight
is_full = False
free_place = 0
command = input()
while command != "Done":
    command = int(command)
    free_place += command
    if free_place >= total_place:
        is_full = True
        break
    command = input()
diff = abs(free_place - total_place)
if is_full:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
