product = input()
product_type = "unknown"
if product == "banana"\
        or product == "apple"\
        or product == "kiwi"\
        or product == "cherry"\
        or product == "lemon"\
        or product == "grapes":
    product = "fruit"
    print("fruit")
elif product == "tomato" \
          or product == "cucumber" \
          or product == "pepper" \
          or product == "carrot":
    product = "vegetable"
    print("vegetable")
else:
    print(product_type)