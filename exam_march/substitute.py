K = int(input())
L = int(input())
M = int(input())
N = int(input())
printed = False
counter_changes = 0

for a1 in range(K, 8 + 1):
    if printed:
        break
    for a2 in range(9, L - 1, -1):
        if printed:
            break
        for b1 in range(M, 8 + 1):
            if printed:
                break
            for b2 in range(9, N - 1, -1):

                if a1 % 2 == 0 and b1 % 2 == 0 and a2 % 2 != 0 and b2 % 2 != 0:
                    if a1 == b1 and a2 == b2:
                        print("Cannot change the same player.")
                    else:
                        print(f"{a1}{a2} - {b1}{b2}")
                        counter_changes += 1
                    if counter_changes == 6:
                        printed = True
                        break