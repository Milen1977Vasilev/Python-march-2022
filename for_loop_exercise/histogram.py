count_numbers =int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for numbers in range(1, count_numbers + 1):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1
percent_p1 = p1/ count_numbers * 100
percent_p2 = p2/ count_numbers * 100
percent_p3 = p3/ count_numbers * 100
percent_p4 = p4/ count_numbers * 100
percent_p5 = p5/ count_numbers * 100
print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")
