import products


class Store:
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = list(products)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for prod in self.products:
            total += prod.get_quantity()
        return total

    def get_all_products(self):
        active_products = []
        for prod in self.products:
            if prod.is_active():
                active_products.append(prod)
        return active_products

    def order(self, shopping_list):
        total_cost = 0.0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost

# Test of class Store

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
