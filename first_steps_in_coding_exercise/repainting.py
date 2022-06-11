needed_nailon = int(input())
needed_paint = int(input())
needed_aceton = int(input())
needed_workers_hours = int(input())
nailon_price = 1.50
paint_price = 14.50
aceton_price = 5.00
total_nailon = nailon_price * (needed_nailon + 2)
total_paint = paint_price * (needed_paint * 1.10)
total_aceton = aceton_price * needed_aceton
torbi = 0.40
total_price = total_paint + total_nailon + torbi + total_aceton
workers_per_hour = (total_price * 0.30) * needed_workers_hours

final_price = total_price + workers_per_hour
print(final_price)