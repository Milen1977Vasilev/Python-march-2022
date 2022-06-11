start_points = int(input())
bonus = 0

if start_points <= 100:
    bonus = 5
elif start_points <= 1000:
    bonus = start_points * 0.20
elif start_points > 1000:
    bonus = start_points * 0.10
if start_points % 2 == 0:
    bonus = bonus + 1
elif start_points % 10 == 5:
    bonus = bonus + 2
total_points = start_points + bonus
print(bonus)
print(total_points)