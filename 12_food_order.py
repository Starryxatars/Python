class FoodOrder:
    TAX_RATE = 0.05

    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        print(f"Order {self.order_id} placed by {self.customer_name}.")

    def calculate_total(self):
        subtotal = self.price * self.quantity
        tax = subtotal * self.TAX_RATE
        return subtotal, tax, subtotal + tax

    def display_bill(self):
        subtotal, tax, total = self.calculate_total()
        print("\n------ Bill ------")
        print(f"Order ID : {self.order_id}")
        print(f"Customer : {self.customer_name}")
        print(f"Item     : {self.food_item} x {self.quantity}")
        print(f"Subtotal : Rs. {subtotal:.2f}")
        print(f"Tax (5%) : Rs. {tax:.2f}")
        print(f"Total    : Rs. {total:.2f}")

    def __del__(self):
        print(f"Order {self.order_id} completed. Thank you, {self.customer_name}!")


order = FoodOrder(1, "Anjali", "Paneer Butter Masala", 2, 220)
order.display_bill()
del order
