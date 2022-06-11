greening_meters = float(input())
meter = 7.61
total_price = greening_meters * meter
final_price = total_price * 0.82
discount = abs(total_price - final_price)
print(f"The final price is: {final_price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")
