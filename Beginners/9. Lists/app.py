cars = ["Lamborghini", "Ferrari", "Mazda", "BMW", "Honda"]

print(cars[1])
print(cars[2])

# bisa pakai minus untuk mengambil value dari belakang
# "-" dimulai dari index -1, dalam lists diatas -1 = "BMW"
print(cars[-1])

# [2:] (index ke 2 dan seterusnya), 1:4 artinya index 1 sampai item ke 4
print(cars[1:4])

cars[1] = "Edited : Avanza"
print(cars)