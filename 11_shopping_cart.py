class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}
        print(f"Shopping cart {self.cart_id} created for {self.customer_name}.")

    def add_product(self, name, price, quantity=1):
        if name in self.products:
            self.products[name][1] += quantity
        else:
            self.products[name] = [price, quantity]
        print(f"Added {quantity} x {name} to the cart.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Removed {name} from the cart.")
        else:
            print(f"{name} not found in the cart.")

    def calculate_total(self):
        return sum(price * qty for price, qty in self.products.values())

    def display_cart(self):
        print(f"\n--- Cart {self.cart_id} ({self.customer_name}) ---")
        for name, (price, qty) in self.products.items():
            print(f"{name:<12} Rs. {price:>8.2f} x {qty} = Rs. {price * qty:.2f}")
        print(f"Total Bill: Rs. {self.calculate_total():.2f}")

    def __del__(self):
        print(f"Shopping cart {self.cart_id} of {self.customer_name} is destroyed.")


cart = ShoppingCart("Anjali", "C101")
cart.add_product("Laptop Bag", 1200, 1)
cart.add_product("Notebook", 50, 4)
cart.add_product("Pen", 10, 5)
cart.display_cart()

cart.remove_product("Pen")
cart.display_cart()

del cart
print("End of program.")
