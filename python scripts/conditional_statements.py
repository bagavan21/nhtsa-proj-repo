#Conditional statements

# IF statement
is_raining = False
print("***IF Condition***")
if is_raining:
    print(f"It's raining!💧, Bring an umbrella.")
#else:
print(f"It's not raining!☀️")   #Without indentation if the line starts from 1st postion it 
print("\n")                      #Python will consider it a new line completly in conditional statements.

# IF ELSE
is_raining = True
print("***IF ELSE Condition***")
if is_raining:
    print(f"It's raining!💧, Bring an umbrella.")
    print("\n")
else:
    print(f"It's not raining!☀️")
    print("\n")


# IF ELIF ELSE
is_raining = True
is_far = True
print("***IF ELIF ELSE Condition***")
if is_raining:
    print(f"It's raining!💧, Drive to the destination.")
    print("\n")
elif is_far:
    print(f"It's far!☀️ but not raining! we can cycle to the destination quickly 🚲.")
    print("\n")
else:
    print(f"No raining!💧, No far!, We can walk to the destination 🚶🏻☀️")
    print("\n")

# Tour planning
is_laves_approved = False
if is_laves_approved:
    print(f"We can go for vacation in summer ☀️")
    print("\n")
else:
    print(f"No vacation for this summer :-( ")
    print("\n")