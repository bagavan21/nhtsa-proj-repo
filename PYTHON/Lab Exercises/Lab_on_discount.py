def apply_discount(price,percent):
    # if discount is 100% or more, price will be free
    if percent >= 100:
        return 0
    else:
    # Other wise, discounted price
        discount = price * percent / 100
        return price - discount
        
# After 10 percent discount
new_price = apply_discount(1000,percent=10)
print(new_price)

# After 5 percent discount
new_price = apply_discount(900,percent=5)
print(new_price)

# After 200 percent discount
new_price = apply_discount(10,percent=200)
print(new_price)