"""Notes."""

#Data type:
name: dict[<key type>, <value type>]
#Example:
temps: dict[str, float]

#Construct an empty dict:
dict() or {}

#Constrct a populated dict:
temps: dict[str, float] = {"Florida": 72.5, "Raleigh": 56.0}

#Adding elements.
temps["DC"] = 52.1 #this adds "DC" with its temperature to the dictionary.

#Removing elements.
temps.pop("DC")

#Access + Modify
temps["DC"] #accesses the value
temps["DC"] = 53.1 #modifies the value

#Checks if key in dictionary
"DC" in temps
"Florida" in temps


"""Practice."""
#Create a dictionary called ice_cream that stores the values below

print("Create a dictionary.")
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

print("Add an element to the dictionary.")
ice_cream["mint"] = 3
print(ice_cream)

print("Remove an element from the dictionary.")
ice_cream.pop("mint")
print(ice_cream)

print(f"There are {ice_cream['chocolate']} orders of chocolate.")
print(ice_cream)

print("Updating the value of vanilla.")
ice_cream["vanilla"] = 10
print(ice_cream)


if "mint" in ice_cream and "chocolate" in ice_cream:
    print("Both mint and chocolate are in ice_cream.")
else:
    print("Mint and chocolate are not in ice_cream.")

if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("No orders of mint.")



for key in ice_cream:
    print(key)

for key in ice_cream:
    print(ice_cream[key])

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")


