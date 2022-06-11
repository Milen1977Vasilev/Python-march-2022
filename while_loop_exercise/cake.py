lenght = int(input())
weight = int(input())
total_pieses = lenght * weight
piese = 0
is_finish = False
command = input()
while command != "STOP":
    command = int(command)
    piese += command
    if piese >= total_pieses:
        is_finish = True
        break
    command = input()
if is_finish:
    print(f"No more cake left! You need {abs(total_pieses - piese)} pieces more.")
else:
    print(F"{abs(total_pieses - piese)} pieces are left." )




