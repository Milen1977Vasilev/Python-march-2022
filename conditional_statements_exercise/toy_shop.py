trip_price = float(input())
puzzle_count  = int(input())
dolls_count  = int(input())
bears_count  = int(input())
minions_count  = int(input())
trucks_count  = int(input())

puzzle_price = puzzle_count * 2.60
doll_price = dolls_count * 3
bear_price = bears_count * 4.10
minion_price = minions_count * 8.20
truck_price = trucks_count * 2

total_win = puzzle_price + doll_price + bear_price +minion_price +truck_price
total_count = puzzle_count + dolls_count + bears_count +minions_count +trucks_count
if total_count >= 50:
    total_win = total_win * 0.75

total_win = total_win * 0.90

diff = abs(total_win - trip_price)
if total_win >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")