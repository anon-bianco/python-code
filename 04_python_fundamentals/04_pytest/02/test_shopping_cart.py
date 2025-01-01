import pytest
from shopping_cart import ShoppingCart


def test_can_add_item_to_cart():
  cart = ShoppingCart(5)
  cart.add("apple")
  assert cart.size() == 1

def test_add_item_and_check():
  cart = ShoppingCart(5)
  cart.add("apple")
  assert "apple" in cart.get_items()

def test_add_more_than_max_item_should_fail():
  cart = ShoppingCart(5)  
  for i in range(5):
      cart.add("apple")

  with pytest.raises(OverflowError):
    cart.add("apple")

def test_can_get_total_price():
  cart = ShoppingCart(5)
  cart.add("apple")
  cart.add("orange")

  price_map = {
    "apple": 2.0,
    "orange": 1.0
  }

  assert cart.get_total_price(price_map) == 3.0