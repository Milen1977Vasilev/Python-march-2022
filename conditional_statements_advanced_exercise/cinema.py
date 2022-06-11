movie_type = input()
rows = int(input())
colons = int(input())
sum = 0
seeds = rows * colons
if movie_type == "Premiere":
    sum = seeds * 12.00
elif movie_type == "Normal":
    sum = seeds * 7.50
elif movie_type == "Discount":
    sum = seeds * 5.00
print(f"{sum:.2f}")
print("leva")