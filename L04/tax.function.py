def get_inputs(quit):
    quit = str.upper(input("Enter Q to quit or any other letter to calculate tax: "))
    price = 0.0
    tax = 0.0
    if quit != 'Q':
        price = float(input("What is the price? "))
        tax = float(input("What is the tax rate? "))
    return quit, price, tax

def calculate_price_with_tax():
    quit = 'T'
    while quit != 'Q':
        quit, price, tax = get_inputs(quit)
        if quit != 'Q':
            final_price = price * (100 + tax) / 100
            print(f"The final price is {final_price}")

    return

calculate_price_with_tax()