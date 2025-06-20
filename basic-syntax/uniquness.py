unique = {x for x in [1, 1, 2, 4, 4, 4, 5, 3, 2, 344, 4, 3, 2, 2, 65, 2]}
print(unique)
# Automatically removes duplicates while creating a set.

squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)
# Creates a dictionary


a, b, * rest = [1, 2, 3, 4, 5]
print(a, b, rest)
# unpacking


def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"


print(greet("Thambi", 25))
# here the type hinting is done
# here the return type is also specified
