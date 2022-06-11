count_locations = int(input())
for location in range(1, count_locations+1):
    gold = 0
    expected_gold = float(input())
    days_count = int(input())
    for day in range(1, days_count + 1):
        current_gold = float(input())
        gold += current_gold
    total_gold_per_day = gold / days_count
    if total_gold_per_day >= expected_gold:
        print(f"Good job! Average gold per day: {total_gold_per_day:.2f}.")
    else:
        print(f"You need {abs(expected_gold-total_gold_per_day):.2f} gold.")