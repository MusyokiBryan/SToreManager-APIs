from flask_restplus import Resource, reqparse, Namespace, fields


class Products(Resource):
    """contains GeT & POST methods"""
    product = Products()

    @staticmethod
    def get():
        response = product.get_all_products()
        return response, 200
