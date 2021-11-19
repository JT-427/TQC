file = open("data.txt", "a")

# TODO
for i in range(5):
    a = input()
    file.write("\n"+a)
file.close()

print("Append completed!")
print('Content of "data.txt":')

# TODO
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()