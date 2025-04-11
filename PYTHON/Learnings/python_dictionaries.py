# DICTIONARY
#################################### simple dictionary ####################################
fruit_prices = {"🍎":1.49, "🍌":0.59, "🫐":3.29}
print(fruit_prices)
print(fruit_prices["🍎"])
print(f"The price of apple is {fruit_prices["🍎"]} CAD")
print(f"The price of banana is {fruit_prices["🍌"]} CAD")
print(f"The price of blueberry is {fruit_prices["🫐"]} CAD")
fruit_prices["🍉"] = 4.29
print(fruit_prices)
#
print(f"The price of watermelon is {fruit_prices["🍉"]} CAD")
#fruit_prices.update({"🍌":0.69})
x = {"🥝":2.89,"🫐":2.29}
print(fruit_prices)
fruit_prices.update(x)                                      # update dictionary
print(fruit_prices)
#
print("\n")
print(len(fruit_prices))                                    # length of the dictionary
cherry_price = fruit_prices.get("🍒")
print(f"The price of cherry is {cherry_price} CAD")

print(fruit_prices.keys())                                      # Returns all the keys in the dictionary
print(fruit_prices.values())                                    # Retuurns all keys of values in the dictionary
print(fruit_prices.items())                                     
print("\n")

print(fruit_prices.get("🍏"))                                # Get an item's value
print(fruit_prices.pop("🍎"))                                # Remove an item
print(fruit_prices.update({"🍎":3}))                        # Add/update items
#fruit_prices.clear()                                        # Removes all items.

print(fruit_prices)
print("\n")

for key in fruit_prices.items():
    print(key)
print("\n")



# JSON
#################################### simple JSON ####################################
import json

shoe = {"name":"Nike Air Force 1", "brand":"Nike","colours": ["red", "blue", "green"], "price":129}

result = json.dumps(shoe)
print(result)
#print(type(result))
print("\n")

# Exersize 
total_expenses = {"food": 40, "transport": 0, "shopping": 190}
#todo: Add an "entertainement" expense ($20)
#todo: Increase "food" expense (by $12)

print(total_expenses) 
print("\n")

total_expenses["food"] += 12
print(total_expenses)
print("\n")

total_expenses["entertainement"] = 20
print(total_expenses)