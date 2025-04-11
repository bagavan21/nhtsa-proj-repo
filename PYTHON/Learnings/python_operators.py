# Assignment operators:
x = 2
print(f"{x} \n")
x += 2
print(f"{x} \n")
x -= 2
print(f"{x} \n")
x *= 2
print(f"{x} \n")

y = 2.5
print(type(y))
print(y, y + 1, y * 2, y ** 2, "\n")

z = 4
print("z value is:", z ** 2)
print(f"z value is: {z ** 2}")

# Comparision Operators
# # == != > < >= <=

x = 2
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# logical operators
# and #AND
# or  #OR
# not #NOT

#Should I go to office on Wednesday?
is_team_coming = True
is_access_granted = False
will_manager_allow = True
print("Should I able to visit office today?",  (is_team_coming and is_access_granted) or will_manager_allow)


#Should i walk to office or drive
distance_meters = 2000
is_raining = False

should_drive = distance_meters < 2000 and is_raining
print("Should i drive to office?",should_drive,"\n")

# let's do a sample exersize
print("#******************SMALL_EXERSIZE******************#")
principal = 240_000
annual_rate = 0.05
years = 2
compound_interest = 0 # Calculate Interest earned!
print(compound_interest)
#formula P * R * T
#simple interest formula P * R * T
interest_earned = principal * annual_rate * years
print("Simple Interest earned in 2 years is", interest_earned)

#compound interest earned in a year
# Compound interest is calculated on the principal amount and also on the accumulated interest of previous periods. 
# This means that interest is earned on interest
compound_interest = principal * (1 + annual_rate) ** years
print("Compound Interest earned in 2 years is", compound_interest)

#################################################################################################
#################################################################################################
#################################################################################################
## Order of operations execution in python 
# 1.Parantheses
# 2.Exponentiation
# 3.Multiplication and Division
# 4.Addition and Substraction
x = 10
y = 3
z = 5
print(x/y)
print("\n")
print(x/z)
print("\n")
print(x//z)
print("\n")
# Example
print("print(2 + 2 * 5 - 3) ==> 2*5 = 10, 10-3=7, 7+2=9  then answer will be 9")
print(2 + 2 * 5 - 3)    # 
print("\n")
print(" print(2 + 2 * (5 - 3)) ==> (5-3)=2, 2*2=4, 4+2=6 then answer will be 6")
print(2 + 2 * (5 - 3))  # 
print("\n")
print("print((2 + 2) * 5 - 3) ==> (2+2)=4, 4*5=20 and 20-3=17 then answer will be 17")
print((2 + 2) * 5 - 3)  # 




a = int(input())
b = int(input())


sum = a + b
print(sum)

diff_val = a - b
print(diff_val)

mult_val = a * b
print(mult_val)
