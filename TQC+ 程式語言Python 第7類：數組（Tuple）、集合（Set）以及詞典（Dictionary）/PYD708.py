#TODO
print("Create dict1:")
dict1 = {}
while True:
    #Key: (後方有一空白格)
    key = input("Key: ")
    if key == "end":
        break
    
    #Value: (後方有一空白格)
    value = input("Value: ")

    dict1[key] = value

print("Create dict2:")
dict2 = {}
while True:
    #Key: (後方有一空白格)
    key = input("Key: ")
    if key == "end":
        break
    
    #Value: (後方有一空白格)
    value = input("Value: ")

    dict2[key] = value

dict1.update(dict2)

for i in sorted(dict1):
    print(i+":", dict1[i])