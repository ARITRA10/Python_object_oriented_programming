# How to create a class
class Item:
    def calculate_total_price(self, x, y):
        return x* y

# How to create an instance of a class
item_1 = Item()

# Assign attributes
item_1.name = "Phone"
item_1.price = 100
item_1.quantity = 5

# Calling methods from instances of a class
print(item_1.calculate_total_price(item_1.price, item_1.quantity))

item_2 = Item()
item_2.name = "Laptop"
item_2.price = 1000
item_2.quantity = 3

print(item_2.calculate_total_price(item_2.price, item_2.quantity))
