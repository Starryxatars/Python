class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, available=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = available

    def rent_vehicle(self, days):
        if not self.available:
            print("Sorry, vehicle is not available.")
            return 0
        self.available = False
        charges = self.calculate_rental(days)
        print(f"Vehicle {self.vehicle_no} rented for {days} day(s).")
        print(f"Rental charges: Rs. {charges:.2f}")
        return charges

    def return_vehicle(self):
        if self.available:
            print("This vehicle was not rented.")
        else:
            self.available = True
            print(f"Vehicle {self.vehicle_no} returned successfully.")

    def calculate_rental(self, days):
        return self.rental_rate * days

    def display(self):
        status = "Available" if self.available else "Rented"
        print(f"Vehicle No  : {self.vehicle_no}")
        print(f"Model       : {self.model}")
        print(f"Rental Rate : Rs. {self.rental_rate:.2f}/day")
        print(f"Status      : {status}")


v = Vehicle("MH12AB1234", "Maruti Swift", 1500)
v.display()

days = int(input("\nEnter number of days to rent: "))
v.rent_vehicle(days)

print()
v.display()

print("\nTrying to rent again:")
v.rent_vehicle(2)

print()
v.return_vehicle()
v.display()
