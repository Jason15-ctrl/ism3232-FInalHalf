# my_tool.py
# Author: Jason Nguyen


class ServicePriceLookup:
    """A tool that looks up nail salon service prices."""

    def __init__(self, prices):
        """Store the service prices."""
        self.prices = prices

    def find_service(self, text):
        """Find a nail service mentioned in a message."""
        for service in self.prices:
            if service in text.lower():
                return service
        return None

    def price_for(self, service):
        """Return the price of a service."""
        return self.prices.get(service)
