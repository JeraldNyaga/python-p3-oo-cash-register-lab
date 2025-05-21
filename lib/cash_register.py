#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
  
  def reset_register_totals(self):
    self.discount = 0
    self.total = 0

  def add_item(self, item: str, cost: float, quantity = 1):
    self.last_item = [item, cost, quantity]
    while quantity:
      self.items.append(item)
      self.total += cost
      quantity -= 1
  def apply_discount(self):
    if self.discount > 0:
      self.total *= (100 - self.discount)/100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  def void_last_transaction(self):
    quantity = self.last_item[2]
    self.total -= (self.last_item[1] * quantity)
    while quantity > 0:
      del self.items[-1]
      quantity -= 1


# cash_register = CashRegister()
# cash_register.add_item("apple", 0.99, 8)
# cash_register.void_last_transaction()