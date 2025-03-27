my_fruits = ("🍎","🍇","🍓")
a,b,c = my_fruits
print(a,b,c)
print("\n")

fav_fruits = {"🍎","🍌","🍇","🍉","🍐"}
season_fruits = {"🥭","🍉","🥑","🍐"}

print("Result of Intersection:")
print(fav_fruits.intersection(season_fruits))
print("\n")
print("Result of union:")
print(fav_fruits.union(season_fruits))
print("\n")
print("Result of difference:")
print(fav_fruits.difference(season_fruits))
print("\n")
print("Result of symmetric_difference:")
print(fav_fruits.symmetric_difference(season_fruits))
print("\n")


# Tuples and sets exersize
user_preference = {"🍔","🍕","🍤"}

restaurants = {
    "sea_food" : {"🍤","🐟","🦀","🍣"},
    "kacks" : {"🍔","🍕","🍟","🍦"},
    "potting" : {"🥦","🥕","🍞","🥑"}
}

for macth_food in restaurants.values():
    print(user_preference.intersection(macth_food))
else:
    print(user_preference.intersection(restaurants["kacks"]))
#macth_food = user_preference.intersection(restaurants["kacks"])
#print(macth_food)