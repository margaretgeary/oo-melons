"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        
        flat_fee = 0
        base_price = 5
        if self.species == "christmas" or self.species == "Christmas":
            base_price = (1.5*base_price)

        if self.order_type == "international" and self.qty < 10:
            flat_fee = 3
        total = ((1 + self.tax) * self.qty * base_price) + flat_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0
        self.order_type = "government"
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
    
        if passed == True:
            self.passed_inspection = True

        return self.passed_inspection