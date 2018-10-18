class Product:
    product_list = []

    def __init__(self, name, description, quantity, category):
        self.product_id = len(self.product_list)+1
        self.product_name = name
        self.product_description = description
        self.product_quantity = quantity
        self.category = category

    def save_product(self):
        product = dict(product_id=self.product_id,
                       product_name=self.product_name,
                       product_description=self.product_description,
                       product_quantity=self.product_quantity,
                       category=self.category
                       )
        self.product_list.append(product)
        return product

    def retrieve_products(self):
        return self.product_list

    def retrieve_single_products(self, productId):
        for product_item in self.product_list:
            if product_item['product_id'] == productId:
                return product_item
        return f"Product of ID {productId} doesn't exist"
