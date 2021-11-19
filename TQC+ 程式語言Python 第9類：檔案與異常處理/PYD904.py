from os import name


data = []

with open("read.txt","r") as file:
   # TODO
   for line in file:
      data.append(line.split())
      print(line)
   
   name = []
   h = []
   w = []
   for i in range(3):
      name.append(data[i][0])
      h.append(eval(data[i][1]))
      w.append(eval(data[i][2]))
   
   print("Average height:", format(sum(h)/3, ".2f"))
   print("Average weight:", format(sum(w)/3, ".2f"))

   print(f"The tallest is {name[h.index(max(h))]} with {format(max(h), '.2f')}cm")
   print(f"The heaviest is {name[w.index(max(w))]} with {format(max(w), '.2f')}kg")






"""
Average height: _
Average weight: _
The tallest is _ with _cm
The heaviest is _ with _kg
"""