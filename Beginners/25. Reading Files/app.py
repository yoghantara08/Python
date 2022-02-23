#r = read
#w = write
#a = append (add)
#r+ = read & write


file_nama = open("C:/Users/user/Desktop/Python/Beginners/25. Reading Files/nama.txt", "r")

for nama in file_nama.readlines():
    print(nama)

# print(file_nama.readable())
# print(file_nama.read())
# print(file_nama.readline())
# print(file_nama.readlines()[2])

# to make sure the file were closed
file_nama.close()