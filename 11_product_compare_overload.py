class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Headphones", 2500)
p2 = Product("Keyboard", 1800)
p3 = Product("Speaker", 2500)

print(f"{p1.name} ({p1.price}) == {p2.name} ({p2.price}) :", p1 == p2)
print(f"{p1.name} ({p1.price}) == {p3.name} ({p3.price}) :", p1 == p3)
print(f"{p1.name} ({p1.price}) >  {p2.name} ({p2.price}) :", p1 > p2)
print(f"{p2.name} ({p2.price}) >  {p1.name} ({p1.price}) :", p2 > p1)
