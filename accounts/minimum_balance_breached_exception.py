
class MinimumBalanceBreachedException(Exception):
    # inherit from built in Exception input - so it can be thrown and caught
    def __init__(self, breach_amount):
        self.breach_amount = breach_amount

    def get_breach_amount(self):
        return self.breach_amount

    def set_breach_amount(self, breach_amount):
        self.breach_amount = breach_amount
