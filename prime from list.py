# Python program to find and print all prime numbers from a given list.

# l = [12, 34, 56, 78, 13, 87, 5]
# for i in l:
#     if i > 1:
#         for j in range(2, i):
#             if i%j == 0:
#                 break
#         else:
#             print(i)



# Python program to print all prime numbers between 1 and 100.

for i in range(1,101):
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i)

