# Assignment 1 
# Ticket pricing rules
############### Rules ###############
### Under 18 - Entry fee is free   ##
### Student or over 65 - 50% off.  ##
### Everyone else pays full price. ##
#####################################
print("############### Movie tickets pricing ###############")
customer_age = 23
is_student = True

if is_student or customer_age > 65:
    print(f"For Student or Senior citizan (age over 65) 🎫 entry is 50% off!")
    print("\n")
elif customer_age < 18:
    print(f"For under age of 18 🎫 entry is FREE!")
    print("\n")
else:
    print(f"Not Student? or age not over 65? Well everyone else 🎫 entry is full-price")
    print("\n")