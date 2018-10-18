""" Sale Rcord Models """


class SaleRecordModel:
    """ Class the defines how our Sale records will look """
    sales_list = []

    def __init__(self, sold_by, unit_price, quantity, category):
        self.sale_id = len(self.sales_list)+1
        self.sale_attendant = sold_by
        self.unit_price = unit_price
        self.product_quantity = quantity
        self.category = category

    def save_record(self):
        """Method to save a sale record"""
        pass

    def retrieve_records(self):
        """ Method to get all  sale records"""
        pass

    def retrieve_single_records(self, saleId):
        """ Method to get one sale record by the sale_record_id"""
        pass
