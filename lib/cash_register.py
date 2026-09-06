#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Validate discount: must be an int between 0 and 100 inclusive
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # Add to total
        self.total += price * quantity
        # Add item(s) to items list
        for _ in range(quantity):
            self.items.append(item)
        # Record this transaction so it can be voided later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        last_transaction = self.previous_transactions.pop()
        # Subtract the price from total
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        # Remove the corresponding items from the items list
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])