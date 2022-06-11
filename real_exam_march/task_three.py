import math

cat = input()
cat_gender = input()
is_invalid = False
months = 12
cat_months = 6

if cat == "British Shorthair":
    if cat_gender == "m":
        months *= 13
    elif cat_gender == "f":
        months *= 14
elif cat == "Siamese":
    if cat_gender == "m":
        months *= 15
    elif cat_gender == "f":
        months *= 16
elif cat == "Persian":
    if cat_gender == "m":
        months *= 14
    elif cat_gender == "f":
        months *= 15
elif cat == "Ragdoll":
    if cat_gender == "m":
        months *= 16
    elif cat_gender == "f":
        months *= 17
elif cat == "American Shorthair":
    if cat_gender == "m":
        months *= 12
    elif cat_gender == "f":
        months *= 13
elif cat == "Siberian":
    if cat_gender == "m":
        months *= 11
    elif cat_gender == "f":
        months *= 12
else:
    is_invalid = True
if is_invalid:
    print(f"{cat} is invalid cat!")
else:
    total_cat_months = months / cat_months
    print(f"{math.floor(total_cat_months)} cat months")





