#cube
# print(2**3) #2^3

def raise_to_power(num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * num
    return result

print(raise_to_power(5,5))