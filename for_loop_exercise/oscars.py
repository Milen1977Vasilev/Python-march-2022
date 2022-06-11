actor_name = input()
points_from_academy = float(input())
judge_count = int(input())
count_points = points_from_academy

for i in range(1, judge_count +1):
    judge_name = input()
    points_from_judge = float(input())

    points = (len(judge_name) * points_from_judge) /2
    count_points = count_points + points

    if count_points > 1250.5:
        break
diff = abs(count_points - 1250.5)
if count_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {count_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")


