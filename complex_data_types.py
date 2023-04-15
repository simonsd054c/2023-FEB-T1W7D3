# List - collection of data - mutable (change) - indexed

names = [ "John", "Jane", "Smith" ]

# print(names)
# names.append("Mike")
# print(names)
# print(names[3])
# names[1] = "Hello"
# print(names)
# names.pop(2)
# print(names)
# insert, pop, remove, sort, reverse, index, count, len


# Tuple - collection of data - immutable (cannot change) - indexed
# days = ( "Monday", "Tuesday", "Wednesday", "Monday" )

# # days.append("Thursday") - cannot use this

# # print(days[1])
# print(days.count("Monday"))
# print(days.count("Tuesday"))

# # count, index similar to list. len 
# print(len(days))


# Set - collection of data - mutable (change) - not indexed - no repeated items

# names = { "John", "Jane", "Smith" }

# print(names)
# names.add("Mike")
# print(names)
# names.remove("John")
# print(names)
# print("Jane" in names)

# a = { 1, 2, 3, 4, 5 }
# b = { 4, 5, 6, 7, 8 }

# # Set Operations - Same as mathematical set operations
# # Union
# u = a.union(b)
# print(u)
# # Intersection
# i = a.intersection(b)
# print(i)
# # Difference
# adb = a.difference(b)
# print(adb)
# bda = b.difference(a)
# print(bda)


# Dictionaries (dicts) - collection of data - mutable - keyed - key value pair

person1 = {
    "name": "John",
    "surname": "Smith",
    "age": 24
}

# print(person1)
# print(person1["name"])
# # get
# # print(person1["address"])
# print(person1.get("address", "Key doesn't exist"))

# person1["age"] = 29
# print(person1)
# person1["address"] = "Sydney"
# print(person1)

# Loop
for key, value in person1.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

print(list(person1.keys()))
print(list(person1.values()))
print(list(person1.items()))
