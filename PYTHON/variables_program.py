item_name = "Pizza"
quantity = 12
price_cad = 10.50
in_stock = True

print(f"item_name = {item_name}")
print(f"quantity = {quantity}")
print(f"price_cad = {price_cad}")
print(f"in_stock = {in_stock}")

# let's make a conversation in a pizza shop
customer = "Sam"
seller = "shop keeper"

cusromer_ask = "We are here for {quantity} {item_name}s, how much is each? and how much for total?"
seller_response = "Yes, {price_cad} is per each {item_name}"
seller_response_2 = "So, it's {price_cad} for each {quantity} {item_name}"
total_price = price_cad * quantity

print(f"{customer} : {cusromer_ask.format(quantity=quantity, item_name=item_name, price_cad=price_cad)}")
print(f"{seller} : {seller_response.format(quantity=quantity, item_name=item_name, price_cad=price_cad)}")
print(f"{seller} : {seller_response_2.format(price_cad=price_cad, quantity=quantity, item_name=item_name)}")
print(f"And, the total price is {total_price} CAD")

cusromer_ask_3 = "Okay, we are good, please arrange it for pick up"
seller_response_3 = "Sure, Thank you for your order and your order will be ready in 15 minutes"
print(f"{customer} : {cusromer_ask_3}")
print(f"{seller} : {seller_response_3}")

print(f"{customer} : Thank you!")