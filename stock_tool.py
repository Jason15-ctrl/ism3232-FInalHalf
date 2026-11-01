# stock_tool.py
# Author: Jason Nguyen


class StockLookup:
    """A tool that checks product inventory."""

    def __init__(self, stock):
        """Store the products and their quantities."""
        self.stock = stock

    def find_product(self, text):
        """Return the first known product mentioned in the message."""
        for product in self.stock:
            if product.lower() in text.lower():
                return product
        return None

    def count_for(self, product):
        """Return the quantity of a product, or None if not found."""
        if product in self.stock:
            return self.stock[product]
        return None
