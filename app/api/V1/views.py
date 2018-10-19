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

    @staticmethod
    def put(product_id):
        parser = reqparse.RequestParser()
        parser.add_argument("product_name", type=str, help="product name should be provided", required=True,
                            location=["json"])

        parser.add_argument("product_price", type=int, help="price should be provided", required=True,
                            location=["json"])
        arguments = parser.parse_args()
        response = product.edit_product(product_id=product_id, product_name=arguments["product_name"],
                                        product_price=arguments["product_price"])
        return response, 201

class Sales(Resource):
    @staticmethod
    def get():
        response = sales_s.see_sales()
        return response, 200

    @staticmethod
    @sales_api.expect(post_a_sale)
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument("product_name", type=str, help="product name should be provided", required=True,
                            location=["json"])

        parser.add_argument("number", type=int, help="number sales should be provided", required=True,
                            location=["json"])

        parser.add_argument("sell_price", type=str, help="price sales should be provided", required=True,
                            location=["json"])
        arguments = parser.parse_args()
        response = sales_s.post_a_sale(product_name=arguments["product_name"],
                                       number=arguments["number"], sell_price=arguments["sell_price"])

        return response, 201

class Sale(Resource):
    @staticmethod
    def get(sale_id):
        response = sales_s.get_a_sale(sale_id=sale_id)
        return response, 200

    @staticmethod
    @sales_api.expect(edit_a_sale)
    def put(sale_id):
        parser = reqparse.RequestParser()
        parser.add_argument("product_name", type=str, help="product name must be provided", location=["json"],
                            required=True)
        parser.add_argument("number", type=int, help="number of products must be provided", location=["json"],
                            required=True)
        parser.add_argument("sell_price", type=int, help="selling price must be provided", location=["json"],
                            required=True)
        args = parser.parse_args()
        response = sales_s.edit_sale(sale_id=sale_id, product_name=args["product_name"], number=args["number"],
                                     sell_price=["sell_price"])
        return response

    @staticmethod
    def delete(sale_id):
        response = sales_s.delete_a_sale(sale_id=sale_id)
        return response

class CreateUsers(Resource):

    @staticmethod
    @user_api.expect(register_user)
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument("user_name", type=str, help="user name should be provided", required=True,
                            location=["json"])

        parser.add_argument("email", type=str, help="email should be provided", required=True,
                            location=["json"])

        parser.add_argument("password", type=str, help="password should be provided", required=True,
                            location=["json"])
        arguments = parser.parse_args()
        response = user.register_user(user_name=arguments["user_name"],
                                      email=arguments["email"], password=arguments["password"])
        return response