def say_hello(title,name):
    message = f" Hello {name.capitalize()} {title.capitalize()}. Welcome to Python"
    return message

##########################
# Positional arguments
print(say_hello("Jack", "Mr"))
print(say_hello("Slice", "Ms"))
print(say_hello("Das", "Dr"))



# exc 1
def double_list_value(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2
    return my_list

prg_list = [1,2,3]
out = double_list_value(prg_list)
print(prg_list)

print(out)


# exc 2
def bank_intreset(principal,rate,years):
    compound_interest = principal * (1 + rate) ** years
    return compound_interest


list_intreset = [240_000,0.05,2]
check_result = bank_intreset(list_intreset[0],list_intreset[1],list_intreset[2])
print(check_result)



#exc 3
def apply_discount(price,percent):
    if percent >= 100:
        return 0
    else:
        discount = price * percent / 100
        return price - discount

new_price = apply_discount(1000,percent=10)
print(new_price)

new_price = apply_discount(900,percent=5)
print(new_price)

new_price = apply_discount(10,percent=200)
print(new_price)



# excersize 
name = input("enter name")
age = int(input("enter age"))

print("Writing to file")
with open("user_info.txt","w") as f:
    f.write(f"{name} {age}\n")

print("Reading file")
with open("user_info.txt","r") as f:
    print(f.read())

print("Appending to file")
with open("user_info.txt","a") as f:
    f.write(f"{name} {age} is just an adult\n")