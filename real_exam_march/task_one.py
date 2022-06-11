import math

speed = float(input())
needed_liters_for_100 = float(input())
distance = 384400

total_distance = distance * 2
sum_distans = math.ceil(total_distance / speed)
total_time = sum_distans +3
fuel = (needed_liters_for_100 * total_distance) / 100
print(total_time)
print(math.ceil(fuel))


