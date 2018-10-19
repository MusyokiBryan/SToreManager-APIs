class Products:
    """Functionality of products"""

    products = {}

    def get_all_products(self):
        """"
        get all products
        """
        if self.products == {}:
            return {"txt": "Product not found"}
        return self.products

    def create_product(self, product_name, product_price):
        new_id = len(self.products) + 1
        self.products[new_id] = {"product_name": product_name,
                                 "product_price": product_price, }
        res = self.products[new_id]
        return {"msg": "Product added successfully", "data": res}

    def get_a_product(self, product_id):
        if self.products == {}:
            return {"txt": "Product not found"}
        return self.products[product_id]

    def delete_a_product(self, product_id):
        del self.products[product_id]
        return {"txt": "Product Deleted"}

    def edit_product(self, product_id, product_name, product_price):
        self.products[product_id] = {"product_id": product_id, "product_name": product_name,
                                     "product_price": product_price}
        return {"msg": "Sale Edited"}


class Sales:
    """Functionality of products"""
    sales = {}

    def see_sales(self):
        if self.sales == {}:
            return {"txt": "No sales added."}
        return self.sales

    def post_a_sale(self, product_name, number, sell_price):
        new_id = len(self.sales) + 1
        self.sales[new_id] = {"product_name": product_name, "number": number,
                              "sell_price": sell_price}
        return {"msg": "added successfully"}

    def get_a_sale(self, sale_id):
        if self.sales == {} or sale_id not in self.sales:
            return {"txt": "No sales added."}
        return self.sales[sale_id]

    def edit_sale(self, sale_id, product_name, number, sell_price):
        self.sales[sale_id] = {"product_name": product_name, "number": number, "sell_price": sell_price}
        return {"msg": "Sale Edited"}

