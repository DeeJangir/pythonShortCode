# way 1
def add_nums(x, y):
    return x + y
print(add_nums(2, 3))
# 5

#way 2
add_nums = lambda x, y: x + y
print(add_nums(2, 3))
# 5

# way 3
print((lambda x, y: x + y)(3, 4))
7