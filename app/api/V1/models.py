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

