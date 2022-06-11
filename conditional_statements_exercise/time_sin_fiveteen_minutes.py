hours = int(input())
minutes = int(input())
total_minutes = (hours * 60) + (minutes + 15)

hour = total_minutes // 60
minute = total_minutes % 60
if hour > 23:
    hour = 0
if minute <= 9:
    print(f"{hour}:0{minute}")
else:
    print(f"{hour}:{minute}")