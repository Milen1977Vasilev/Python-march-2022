import math

tournament_count = int(input())
start_point = int(input())

w = 0
f = 0
sf = 0
win_count = 0
for games in range(1, tournament_count + 1):
    stage = input()
    if stage == "W":
        w += 2000
        win_count += 1
    elif stage == "F":
        f += 1200
    elif stage == "SF":
        sf += 720
total_points = start_point + w + f + sf
middle_points = (w + f + sf) / tournament_count
win_percent = (win_count / tournament_count) * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(middle_points)}")
print(f"{win_percent:.2f}%")
