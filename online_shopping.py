class Product:
    def __init__(self, product_name, price, quantity_in_stock):

# instance variables       
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

# Displays all Product details in the store
    def display_product_info(self):
        print(f"Product: {self.product_name} ")
        print(f"Price: {self.price} ")
        print(f"Quantity_in_stock: {self.quantity_in_stock}")




class ShoppingCart:
# Class variable to track the total number of shopping carts created
    total_carts = 0

# constructor 
    def __init__(self):
#instance variables        
        
 # Each item in the list is a tuple (Product, quantity)        
        self.items = [] 
        ShoppingCart.total_carts += 1

# adding items to cart
    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"{quantity} {product.product_name} added to cart.")
        else:
            print("Insufficient stock.")

# removing added items from cart
    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"{product.product_name} not found in the cart.")

# display all items from cart 
    def display_cart(self):
        if not self.items:
            print("Epmty cart, add items.")
        else:
            print("ShoppingCart: ") 
            for product, quantity in self.items:
                print(f"{product.product_name},  quantity: {quantity},  price per unit: shs.{product.price}")    

# Calculates and returns the total price of items in the cart.
    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total
    
# create instances  of product  
product1 = Product("Iphone 15", 5000000, 10 )
product2 = Product("SamsungNote 10+", 700000, 1 )
product3 =Product("HP Laptop", 2000000, 4 )
product4 =Product("Type-c Charger", 50000, 5)
product5 =Product("FountainPens", 5000, 6)

# Display product information
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()
product4.display_product_info()


# creating two Shopping Carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()


# adding items to cart
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 4)
cart2.add_to_cart(product4, 2)
cart2.add_to_cart(product5, 5)

# Remove an item from cart1
cart1.remove_from_cart(product1)
cart1.display_cart()

# calculate total for cart1 after removal
print(f"Total for Cart 1 after removal: shs.{cart1.calculate_total()}")

# Display cart contents and calculate total
print("Cart 1:",  cart1.display_cart())
print("Total:", cart1.calculate_total())

print("Cart 2:",  cart2.display_cart())
print("Total:", cart2.calculate_total())



