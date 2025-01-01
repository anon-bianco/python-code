from typing import List

class ShoppingCart:
  def __init__(self, max_size):
    self.items = []
    self.max_size = max_size

  def add(self, item):
    if self.max_size == self.size():
      raise OverflowError("cannot add more item")
    self.items.append(item)

  def size(self):
    return len(self.items)

  def get_items(self) -> List[str]:
    return self.items

  def get_total_price(self, price_map):
    total_price = 0
    for item in price_map:
      total_price += price_map.get(item)
    return total_price
