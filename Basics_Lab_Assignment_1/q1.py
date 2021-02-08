# Q1
def print_type(type__):
    if type(type__) is set:
        print("set now: ")
    elif type(type__) is tuple:
        print("tuple now: ")
    elif type(type__) is dict:
        print("dictionary now: ")
    elif type(type__) is list:
        print("list now: ")
    print(type__)


myList = [1, 2, 3, 4, 5, 6]
myTuple = ("a", "bcd", 1, 2)
myDict = {
    1: "Hello",
    2: "World",
    3: "!!!",
    4: "How are",
    5: "You?",
}
mySet = {"apple", "orange", 1, 2, 2, "apple"}

print("The list is:")
print(myList)
print("The tuple is:")
print(myTuple)
print("The dictionary is:")
print(myDict)
print("The set is:")
print(mySet)

# SET OPERATIONS
mySet.add("banana")
mySet.add(True)
print_type(mySet)
mySet.remove("apple")
print_type(mySet)

# DICTIONARY OPERATIONS
myDict[5] = "Hola"
print_type(myDict)
myDict[6] = "I am fine, thankYou"
print_type(myDict)
myDict.pop(3)
print_type(myDict)

# LIST OPERATIONS
myList.append(23)
print_type(myList)
myList[6] = "Hello"
print_type(myList)
myList.remove(3)
print_type(myList)

# TUPLE OPERATIONS
(val1, val2, val3, val4) = myTuple
print("After unpacking tuple: ")
print(val1, val2, val3, val4)