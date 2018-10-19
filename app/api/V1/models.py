
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