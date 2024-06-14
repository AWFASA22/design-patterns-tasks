import random

class Product:
    def __init__(self, name, price, discount=0, initial_stock=0, reorder_threshold=10, demand_forecast=0):
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = initial_stock
        self.reorder_threshold = reorder_threshold
        self.demand_forecast = demand_forecast
        self.price_history = [(price, 'Initial Price')]  # List of tuples (price, reason)

    def get_price_after_discount(self):
        return self.price * (1 - self.discount)
    
    def update_stock(self, quantity):
        self.stock += quantity
        print(f"Updated stock for {self.name}: {self.stock}")
    
    def calculate_reorder_point(self):
        # Simple calculation based on demand forecast
        reorder_point = self.demand_forecast * 1.5  # Assume 1.5x the forecast as a safety measure
        self.reorder_threshold = max(self.reorder_threshold, reorder_point)
        print(f"Reorder point for {self.name} set to: {self.reorder_threshold}")
        return self.reorder_threshold
    
    def needs_reordering(self):
        if self.stock <= self.reorder_threshold:
            print(f"Product {self.name} needs reordering.")
            return True
        else:
            print(f"Product {self.name} does not need reordering.")
            return False
    
    def adjust_price(self, market_trend_factor):
        # Simulate price adjustment based on market trend factor
        new_price = self.price * market_trend_factor
        self.price = new_price
        self.price_history.append((new_price, 'Market Trend Adjustment'))
        print(f"Adjusted price for {self.name}: ${self.price:.2f}")

    def get_price_history(self):
        return self.price_history

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
   
    product1 = Product("Laptop", 1000, 0.1, initial_stock=50, demand_forecast=20)
    product2 = Product("Mouse", 50, initial_stock=100, demand_forecast=30)
    product3 = Product("Keyboard", 80, 0.05, initial_stock=75, demand_forecast=15)

    
    product1.update_stock(20)  
    product2.update_stock(-10)  
    product3.update_stock(-80)  

    product1.calculate_reorder_point()
    product2.calculate_reorder_point()
    product3.calculate_reorder_point()

    product1.needs_reordering()
    product2.needs_reordering()
    product3.needs_reordering()

    market_trend_factor = random.uniform(0.8, 1.2)  
    product1.adjust_price(market_trend_factor)
    product2.adjust_price(market_trend_factor)
    product3.adjust_price(market_trend_factor)

    print(f"Price history for {product1.name}: {product1.get_price_history()}")
    print(f"Price history for {product2.name}: {product2.get_price_history()}")
    print(f"Price history for {product3.name}: {product3.get_price_history()}")

    customer = Customer("Awfa", "Awfa@example.com")

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
