# Learning Python Dictionaries
car = {
    "brand": "FORD",
    "model": "Mustang",
    "year": 1964,
}

# Two ways to get value of model
x = car["model"]
x = car.get("model")

# Get all of the keys in the dict
x = car.keys()
print(x)

# Add new value to the dictionary
car["colour"] = "white"

# update value of dict
car["year"] = 2020
x = car.values()
print(x)

# Get a list of the key : value pairs
x = car.items()

# check if key is in the dictionary
if "model" in car:
    print("Yes,  'model' is one of the keys in this dict")


# Update Dic
car.update({"year": 2023})

# Remove items from a dictionary

car.pop("model")
# car.popitem() <- removes last inserted item py 3.8 >
# del car["model"] <- removes model from dict
# del car.clear() <- empties dictionary

# Loop through keys in dictionary
for x in car:
    print(x)
# Loop through values in dictionary
for x in car:
    print(car[x])

for x in car.values():
    print(x)

for x in car.keys():
    print(x)


for x, y in car.items():
    print(x, y)


# Copy a Dictionary

car2 = car.copy()

car3 = dict(car2)
print(car3)
