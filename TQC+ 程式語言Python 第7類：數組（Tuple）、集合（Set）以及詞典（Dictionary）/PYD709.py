#TODO

color_dict = {}
while True:
    #Key: (後方有一空白格)
    key = input("Key: ")
    if key == "end":
        break
    
    #Value: (後方有一空白格)
    value = input("Value: ")

    color_dict[key] = value

for i in sorted(color_dict):
    print(i+":", color_dict[i])