#---------------------------1---------------------------#
# a. The first 3 letters are displayed
# b. The last 3 letters are displayed
# c. Pol...nic

# Initialize the string
string = "Polytechnic"

# Display the result
print("%s...%s" % (string[0:3], string[len(string) - 3 : len(string)]))

#---------------------------2---------------------------#
# a. There is an error because cat cannot be converted to a float
# b. Input: 88.99
#    output: 88 dollars 99 cents
# c. No, there is no change in the output

# Gather input from the user
price = float(input("Enter a price: "))

# Compute the dollars and the cents
dollars = int(price)
cents = int((price - dollars) * 100 + .5)

# Display the results
print(dollars, "dollars", cents, "cents")
# Same print with an f string
print(f"{dollars} dollars {cents} cents")

#---------------------------3---------------------------#
# a. It removes Ann from the list
# b. At the very end (where Ann was located)
# c. names.sort()
# d. ['Fritz', 'Jorge', 'Melina']

# Create a list. List methods allow you to manipulate
names = ["Fritz"]
names.insert(1, "Ann")
names.insert(0, "Melina")
names.pop(2)
names.append("Jorge")
print(names)
names.sort()
print(names)

#---------------------------4---------------------------#
# a. Brian has new number 5551212

# Create a dictionary of key:value pairs
contacts = {"Jenny": 8675309, "James": 5551212}
print(*contacts)
print("Jenny's number is", contacts["Jenny"])
brian = contacts.get("James")
print("Brian has new number", brian)