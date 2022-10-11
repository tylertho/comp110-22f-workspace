"""Demonstrations of dictionary capabilities."""


# declaring the type of a dictionary
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# pring a dictionary literal representation
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# test for the existence of a key
if "Duke" in schools:
    print("Foudn the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# CANNOT HAVE DUPLICATE KEYS
# CAN HAVE DUPLICATE VALUES

print(schools)

# demonstration of dictionary literals

# empty dictionary literal
schools = {} # same as dict()

# alternatively initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# what happens when a key does not exist?
print(schools["UNCC"])
