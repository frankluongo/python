def add_numbers(x, y):
    return x + y
add_numbers(1,2)
print(f"The sum of 1 and 2 is {add_numbers(1,2)}")

x = 1
y = 2
def add_numbers(x, y):
    print(f"Inside the function, x = {x} and y = {y}")
    return x + y
print(f"Outside the function, x = {x} and y = {y}")
print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")
