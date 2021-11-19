#TODO
dict1 = {}
while True:
    #Key: (後方有一空白格)
    key = input("Key: ")
    if key == "end":
        break
    
    #Value: (後方有一空白格)
    value = input("Value: ")

    dict1[key] = value
ser = input("Search key: ")

if ser in dict1:
    print(True)
else:
    print(False)