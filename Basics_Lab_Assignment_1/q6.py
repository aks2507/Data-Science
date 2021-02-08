# Q6
print("Enter string: ")
string = input()
str__ = string.lower()
myDict = {}
for i in str__:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1

print("Following is the count:")
print(myDict)

