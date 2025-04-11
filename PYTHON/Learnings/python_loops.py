# Loops
list_of_fruits = ["Banana","Apple","Orange","Pear"]
for fruit in list_of_fruits:
    print(f"The fruit is {fruit}")
    print(f"it's healthy and tasty")
print(f"Thanks for the fruit!")
print("\n")

# Enumerator        ==> it returns in pair like list sequence,list value ex (0,Banana), (1,Apple) etc..
for i in enumerate(list_of_fruits):
    print(i)

# for loop in range
for x in range(0, 101, 50):
    print(f"The number is {x}")
print("\n")

# WHILE LOOP
while True:
    print(f"This will always repeats!")
    break
print(f"welcome back!")
print("\n")

# While scnario 1
print("While scnario 1")
count = 0
while True:
    count += 1
    if count == 1 or count == 3 or count == 5 or count == 7 or count == 9:
        continue
    print(f"This has run {count} times!")
    if count == 10:
        break
print("\n")

# While scnario 2
print("While scnario 2")
for i in range(10):
    if i == 3:
        continue
    print(f"This has run {i} times!")
    if count == 5:
        break
print("\n")


# while scenario 3
print("While scnario 3")
count = 0
while count < 5:                    # insted of while True or Flase, we can also use logical condition
    count +=1
    print(f"This has run {count} times!")
print("\n")


# Comprehensions 
my_list = [2,4,6,0,1]
new_list = [2 * x for x in my_list]
print(new_list)
print("\n")

# other way to multiply
new_list = []
for x in my_list:
    new_list.append(2 * x)
print(new_list)
print("\n")

# loop excersize
# print the following pattern using for loop:
#0
#0 1
#0 1 2
#0 1 2 3
#0 1 2 3 4
#print("\n")
print("# print the following pattern using for loop:")
for x in range(5):
    message = ""
    for y in range(x + 1):
        message += f"{y} "
        print(message)
print("\n")


## Leap year
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
            
    return leap

year = int(input())
print(is_leap(year))