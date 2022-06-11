age = int(input())
price_wash = float(input())
price_toys = int(input())
brother = 0
money_save = 0
toys_count = 0
for ages in range(1 , age + 1):
    if ages % 2 == 0:
        money_save += (ages * 10) / 2
        brother += 1
    else:
        toys_count += 1
total_price_toys = toys_count * price_toys
total_money_save = money_save + total_price_toys - brother
diff = abs(total_money_save - price_wash)
if total_money_save >= price_wash:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


