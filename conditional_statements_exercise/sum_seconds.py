time_first = int(input())
time_second = int(input())
time_third = int(input())

sum_time = time_third + time_second + time_first

minutes = sum_time // 60
seconds = sum_time % 60

if seconds < 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")