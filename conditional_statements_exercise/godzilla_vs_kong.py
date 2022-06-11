budget = float(input())
statist_count = int(input())
price_dress = float(input())

decor_price = budget * 0.10
all_price_dress = statist_count * price_dress
if statist_count > 150:
    all_price_dress = all_price_dress * 0.90
total_cost = decor_price + all_price_dress
diff = abs(budget - total_cost)
if total_cost <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")