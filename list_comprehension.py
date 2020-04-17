n = 20
print([num for num in range(n)])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print([num for num in range(1, n + 1)])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print([num for num in range(1, n, 2)])
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print([num if num%3==0 else "nan" for num in range(10)])
# [0, 'nan', 'nan', 3, 'nan', 'nan', 6, 'nan', 'nan', 9]
print([num for num in range(n) if num%4==0])
# [0, 4, 8, 12, 16]