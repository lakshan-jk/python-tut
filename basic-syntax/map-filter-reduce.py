from functools import reduce
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
product = reduce(lambda x, y: x * y, nums)
print(squared)
print(evens)
print(product)
