import os

# if os.path.isfile("write.txt"):
file = open("write.txt", "w")
for i in range(5):
    a = input()
    file.write(a+"\n")

file.close



# TODO