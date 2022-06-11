packet_pen_count = int(input())
packet_market_count = int(input())
cleaning_count = int(input())
discount = int(input())
pen_price = 5.80
marker_price = 7.20
cleaning = 1.20
total_pen_price = packet_pen_count * pen_price
total_market_price = packet_market_count * marker_price
total_cleaning_price = cleaning_count * cleaning
total_price = total_cleaning_price + total_market_price + total_pen_price
final_price = total_price - (total_price * discount/ 100)
print(final_price)