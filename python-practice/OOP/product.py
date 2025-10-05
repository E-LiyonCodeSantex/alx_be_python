class products:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_porduct_name(self):
        product_full_details = f"name: {self.name} price: {self.price} quantity: {self.quantity}"
        return product_full_details
    
    def cal_product_total_price(self):
        total_price = f"total price is: {self.price * self.quantity}"
        return total_price
    
product1 = products("laptop", 200000, 2)
print(product1.get_porduct_name())
print(product1.cal_product_total_price())