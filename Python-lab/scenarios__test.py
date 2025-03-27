#Exercise 1
##########################################################################################################
# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.
print("########## Exercise 1 ##########")
def multiplcation(num1, num2):
    product = num1 * num2
    return product

    if product <= 1000:
        print(product)
    else:
        print(num1 + num2)

result = multiplcation(20, 30)
print(result)

result = multiplcation(40, 30)
print(result)
print("\n")


#Exercise 2
########################################################################################################## 
#Print the Sum of a Current Number and a Previous number
#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
print("########## Exercise 2 ##########")
print("Printing current and previous number sum in a range(10)")
previous_num = 0

# loop from 1 to 10

for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i
print("\n")


#Exercise 3
##########################################################################################################
#Print characters present at an even index number
#Write a Python code to accept a string from the user and display characters present at an even index number.
#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
# accept input string from a user
print("########## Exercise 3 ##########")
word = "Python_3_version" #input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])
print("\n")


#Exercise 4
##########################################################################################################
#Remove first n characters from a string
#Write a Python code to remove characters from a string from 0 to n and return a new string.

#For Example:
#remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
#remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
print("########## Exercise 4 ##########")
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]                # If colun keep in before n then chars will remove RHS 
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
print("\n")


#Exercise 5
##########################################################################################################
def getMinimumStress(graph_nodes, graph_from, graph_to, graph_weight, source, destination):
    import heapq
    import sys
    
    # Create an adjacency list for the graph
    adj_list = [[] for _ in range(graph_nodes + 1)]
    for i in range(len(graph_from)):
        adj_list[graph_from[i]].append((graph_to[i], graph_weight[i]))
        adj_list[graph_to[i]].append((graph_from[i], graph_weight[i]))  # Since it's an undirected graph
    
    # Initialize distances and priority queue
    distances = [sys.maxsize] * (graph_nodes + 1)
    distances[source] = 0
    pq = [(0, source)]  # (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we reached the destination, return the distance
        if current_node == destination:
            return current_distance
        
        # If we found a shorter path to the current node, skip processing
        if current_distance > distances[current_node]:
            continue
        
        # Process neighbors
        for neighbor, weight in adj_list[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # If we never reach the destination, return -1 or any other value indicating no path
    return -1

# Example usage
graph_nodes, graph_edges = (5, 6)
graph_from = [1, 1, 2, 3]
graph_to = [2, 3, 4, 5]
graph_weight = [2, 3, 1, 4]
source = 5
destination = 6

result = getMinimumStress(graph_nodes, graph_from, graph_to, graph_weight, source, destination)
print(result)  # Output: 7
print("\n")

#Exercise 6
##########################################################################################################
#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
######Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    n = int(input("Enter the number of commands: "))
    
# Initialize the list
my_list = []

# Iterate through the commands
for _ in range(n):
    command = input().split()  # Read and split the command
    cmd = command[0]           # Command type
    
    if cmd == "insert":
        i, e = int(command[1]), int(command[2])
        my_list.insert(i, e)
    elif cmd == "print":
        print(my_list)
    elif cmd == "remove":
        e = int(command[1])
        my_list.remove(e)
    elif cmd == "append":
        e = int(command[1])
        my_list.append(e)
    elif cmd == "sort":
        my_list.sort()
    elif cmd == "pop":
        my_list.pop()
    elif cmd == "reverse":
        my_list.reverse()
print("\n")