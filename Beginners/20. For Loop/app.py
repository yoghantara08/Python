from tkinter import Y


for letter in "Python For Loop":
    print(letter)

array = ["Andy", "Bobi", "Esta", "Yoda"]
for arr in array:
    print(arr)

numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

for index in range(3, 10):
    print(index)

#len() length
for arr in range(len(array)):
    print(array[arr])

for i in range(5):
    if i == 0:
        print("first Iteration")
    else:
        print("not first")

#break = stop / out from the loop
for x in range(5):
    print(x)
    if x == 3:
        break

#continue = stop at the statement and continue
for y in ["A", "B", "C", "D", "E"]:
    if y == "C":
        continue
    print(y)