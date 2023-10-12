#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity=0):
        last_item = title
        self.total += price * quantity if quantity > 0 else price
        self.last_transaction.append(price * quantity if quantity > 0 else price)
        q = range(quantity)
        if quantity > 0:
            for n in q: self.items.append(last_item)
        else:
            self.items.append(last_item)
        return self.total

    def apply_discount(self):
        self.total -= int(self.total * self.discount / 100)
        if self.discount > 0:
            print(f"After the discount, the total comes to ${self.total}.") 
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction[-1]



# test = CashRegister()
# test.add_item("apple", 1)
# test.add_item("banana", 2)
# print(test.items)