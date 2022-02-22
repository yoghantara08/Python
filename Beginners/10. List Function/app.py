numbers = [10,2,21,6,8,12,]
cars = ["Lamborghini", "Ferrari", "Lamborghini", "Mazda", "BMW", "Honda"]

#1. extend() adding lists to lists
cars.extend(numbers) 
print(cars)

#2. append() add an item to the end of the lists
cars.append("Append function")
print(cars)

#3. insert() inserting an item after a spesific index
cars.insert(1, "Insert function")
print(cars)

#4. remove() remove an item in lists
cars.remove("BMW")
print(cars)

#5. pop() pop / remove the last item in the lists
cars.pop()
print(cars)

#6. index() searching the spesific index of an item in the lists
print(cars.index("Honda"))

#7. count() count how many times the value of specific items are in the lists
print(cars.count("Lamborghini"))

#8. sort() sort a lists to descending order
tes_sort = ["Freddy", "Alex", "Dorian", "Harry"]
print(tes_sort)
tes_sort.sort()
print(tes_sort)

print(numbers) 
numbers.sort()
print(numbers) 

#9. reverse() reverse a lists
tes_reverse = ["Tes 1", "Tes 2", "Tes 3"]
print(tes_reverse)
tes_reverse.reverse()
print(tes_reverse)

#10. copy()
alphabet = ["A", "B", "C", "D"]
tes_copy = alphabet.copy()
print(alphabet)
print(tes_copy)

#11. clear() clearing a lists
numbers.clear()
print(numbers)