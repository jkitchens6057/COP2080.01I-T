def add_mult(x, y):
    return x+y, x*y

print(add_mult(10,20))

add_mult_lambda = lambda x, y: (x+y, x*y)

print(add_mult_lambda(10, 20))