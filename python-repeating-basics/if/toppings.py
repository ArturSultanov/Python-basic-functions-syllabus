requested_toppings = ['mushrooms', 'onios', 'olives',
                      'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings =[]

if requested_toppings:
    for topping in requested_toppings:
        if topping == 'onios':
            print(f"Sorry! We don't have {topping}.")
        elif topping == 'pineapple':
            print(f"Adding {topping.title()}, but know that it's so weird!")
        else:
            print(f"Adding {topping.title()}.")
else:
    print("Are you sure you want a plain pizza?")
            
