# 1. 1,2,3,4,5
for i in range(1, 6):
    print(i)


# 2. 1,3,5,7,9,11
for i in range(1, 12, 2):
    print(i) 

# 3. 2,4,6,8,10
for i in range(2, 11, 2):
    print(i)


# 4. 100,200,300,400,500
for i in range(100, 501, 100):
    print(i)


# 5. 5,4,3,2,1
for i in range(5, 0, -1):
    print(i)


# 6. 3,6,9,12,15,18,21
for i in range(3, 22, 3):
    print(i)


# 7. 1,4,9,16,25,36 (Squares)
for i in range(1, 7):
    print(i**2)


# 8. Print all 3-digit numbers (100-999)
for i in range(100, 1000):
    print(i)


# 9. Print all numbers divisible by 3 in the range 100-200
for i in range(100, 201):
    if i % 3 == 0:
        print(i)


# 10. 1,8,27,64,125 (Cubes)
for i in range(1, 6):
    print(i ** 3)