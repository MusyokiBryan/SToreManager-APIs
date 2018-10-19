from flask_restplus import Resource, reqparse, Namespace, fields


class Products(Resource):
    """contains GeT & POST methods"""
    product = Products()

    @staticmethod
    def get():
        response = product.get_all_products()
        return response, 200

    @product_api.expect(create_product)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("product_name", type=str, help="product name should be provided", required=True,
                            location=["json"])

        parser.add_argument("product_price", type=int, help="price should be provided", required=True,
                            location=["json"])
        arguments = parser.parse_args()
        response = product.create_product(product_name=arguments["product_name"],
                                          product_price=arguments["product_price"])
        return response, 201


class Product(Resource):
    """contains GeT, DeL & PUT methods"""

    @staticmethod
    def get(product_id):
        response = product.get_a_product(product_id=product_id)
        return response, 200

    @staticmethod
    def delete(product_id):
        response = product.delete_a_product(product_id=product_id)
        return response, 204
