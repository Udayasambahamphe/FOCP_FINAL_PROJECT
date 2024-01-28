pizza_price = 12
delivery_cost = 2.5
is_tuesday_discount = 0.5
app_discount = 0.75

def calculate_total_price(num_pizzas, is_tuesday, is_delivery, used_app):
    # Apply delivery cost if less than 5 pizzas are ordered and delivery is needed
    delivery_cost = 2.5 if num_pizzas < 5 and is_delivery else 0
    total_price = num_pizzas * pizza_price + delivery_cost

    if is_tuesday:
        total_price *= is_tuesday_discount  

    if used_app:
        total_price *= app_discount  

    return round(total_price, 2)

print("BPP Pizza Shop")
print("BPP Pizza Price")
print("===========================")

# Loop to get the number of pizzas
while True:
    try:
        num_pizzas = int(input("How many pizzas ordered? "))
        if num_pizzas > 0:
            break
        else:
            print("Wrong input! Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

while True:
    is_delivery = input("Is delivery required? (y/n) ").lower()
    if is_delivery in ['y', 'n']:
        break
    else:
        print('Please answer "y" or "n".')

while True:
    is_tuesday = input("Is it Tuesday? (y/n) ").lower()
    if is_tuesday in ['y', 'n']:
        break
    else:
        print('Please answer "y" or "n".')

while True:
    used_app = input("Did the customer use the app? (y/n) ").lower()
    if used_app in ['y', 'n']:
        break
    else:
        print('Please answer "y" or "n".')

# Calculate the total price based on the inputs
total_price = calculate_total_price(num_pizzas, is_tuesday == 'y', is_delivery == 'y', used_app == 'y')

# Display the total price
print("\nTotal Price: £{:.2f}".format(total_price))

