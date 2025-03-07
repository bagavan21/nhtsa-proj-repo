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
