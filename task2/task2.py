class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount
    
    def get_price_after_discount(self):
        return self.price * (1 - self.discount)

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product, quantity=1):
        self.products.append((product, quantity))

    def calculate_total_cost(self):
        total = 0
        for product, quantity in self.products:
            total += product.get_price_after_discount() * quantity
        return total

    def generate_invoice(self):
        invoice = f"Invoice for {self.customer.name} ({self.customer.email})\n"
        invoice += "----------------------------------------\n"
        total_cost = 0

        for product, quantity in self.products:
            cost = product.get_price_after_discount() * quantity
            total_cost += cost
            invoice += f"{product.name} (x{quantity}): ${cost:.2f} "
            if product.discount > 0:
                invoice += f"(Discounted from ${product.price:.2f})"
            invoice += "\n"
        
        invoice += "----------------------------------------\n"
        invoice += f"Total Cost: ${total_cost:.2f}\n"
        return invoice

# Example Usage
if __name__ == "__main__":
    # Creating Products
    product1 = Product("Laptop", 1000, 0.1)  # 10% discount
    product2 = Product("Mouse", 50)
    product3 = Product("Keyboard", 80, 0.05)  # 5% discount

    # Creating a Customer
    customer = Customer("Awfa ", "Awfa@example.com")

    # Creating an Order
    order = Order(customer)
    order.add_product(product1, 1)
    order.add_product(product2, 2)
    order.add_product(product3, 1)

    # Adding order to the customer's orders list
    customer.add_order(order)

    # Calculating Total Cost
    print(f"Total Cost: ${order.calculate_total_cost():.2f}")

    # Generating Invoice
    print(order.generate_invoice())
