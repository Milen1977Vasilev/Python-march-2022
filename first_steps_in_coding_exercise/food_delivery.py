chicken_menu_count = int(input())
fish_menu_count = int(input())
vegan_menu_count = int(input())

chicken_menu_price = chicken_menu_count * 10.35
fish_menu_price = fish_menu_count * 12.40
vegan_menu_price = vegan_menu_count * 8.15

all_menu_price = chicken_menu_price + fish_menu_price + vegan_menu_price
desert = all_menu_price * 0.20
total_delivery_price = all_menu_price + desert + 2.50
print(total_delivery_price)