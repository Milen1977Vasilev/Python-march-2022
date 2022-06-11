import math

processors_count = int(input())
workers_count = int(input())
working_days = int(input())
price = 110.10
loses = 0
wins = 0
worker_hour_per_day = 8
processor_per_hour = 3
total_hours = workers_count * working_days * worker_hour_per_day
total_processors = math.floor(total_hours / processor_per_hour)
sum_processors = abs(processors_count - total_processors)
if total_processors < processors_count:
    print(f"Losses: -> {sum_processors * price:.2f} BGN")
else:
    print(f"Profit: -> {sum_processors * price:.2f} BGN")






