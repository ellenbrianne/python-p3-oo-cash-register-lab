#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=[]):
        self.discount = discount
        self.total = total
        self.items = items

    def add_item(self, title, price):
        pass