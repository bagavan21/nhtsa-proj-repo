############################## LISTS ##############################
# COLLECTION OF ITEMS #
# shopping products
# TV episodes
# Items in a game
# Example
list_of_fruits = ["Banana","Apple","Orange","Pear"]
print(list_of_fruits)
print(list_of_fruits[0])
print(list_of_fruits[1])
print(list_of_fruits[2])
print(list_of_fruits[3])
print("\n")

# Example2
# Items do not have to be relates
list_details = ["apple", 1, True]
print(list_details)

# Acc
print(list_details[0])
print(list_details[1])
print(list_details[2])
print("\n")

############################## 2D LIST ##############################
grid = [[0,1,0],[1,2,3]]
print(grid)
print(grid[0][0])
print(grid[1][2])
print(grid[0])
print(grid[1])
print("\n")


############################## LIST OPERATIONS ##############################
# Create an empty list
empty_list = []
print(empty_list)
empty_list.append("apple")
empty_list.append("banana")
empty_list.append("cherry")
print(empty_list)
print(empty_list[0])
print(empty_list[1])
print("\n")

# how many items are in the list
print(len(empty_list))
print("\n")

# remove an item by value.
empty_list.remove("banana")
print(empty_list)
print("\n")

# remove the list item from a list
empty_list.pop(0)
print(empty_list)
print("\n") 


# create an empty list with Example 3
empty_list = []
print(empty_list)
empty_list.append("apple")
empty_list.append("cherry")
empty_list.append("banana")
print(empty_list)
print(empty_list[0])
print(empty_list[1])
print(empty_list[2])
print("\n")

# pop() also can store with end of the list value
fruit = empty_list.pop()
print(fruit)
print(empty_list)
print("\n")

# Using a negative Index
indoor_games = ["shuttle","basketball","tennis","squash","ping pong","pool","carroms"]
indoor_games.sort()
print(indoor_games[-1])
print("\n")

# REVERSE SORT SLICING[1:3]
slice_indoor_games = indoor_games[0:3]   #sliced 0:3 ==> 0,1,2
print(slice_indoor_games)
print("\n")
indoor_games.reverse()
print(indoor_games)
print("\n")

print("mytest")
lt = [1,2,3,4,5,0]
print(lt[5])
# sort list
lt.sort() # ==> [0,1,2,3,4,5]

# reverse list
lt.reverse() # ==> [5,4,3,2,1,0]

# slice list 
lt_slice = lt[0:3] # ==> [5,4,3]
print(lt_slice)
print("\n")
