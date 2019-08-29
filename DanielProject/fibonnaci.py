arr_length = int(input("Enter the length of Fibonacci numbers array: "))
fibonacci = [0, 1]
pointer_1 = 0
pointer_2 = 1

while len(fibonacci) <= arr_length:
    fibonacci.append(pointer_1 + pointer_2)
    spear = pointer_1
    pointer_1 = pointer_2
    pointer_2 = spear + pointer_2

print(fibonacci)
