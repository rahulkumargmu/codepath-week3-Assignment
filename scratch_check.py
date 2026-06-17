"""Temporary scratch check for models.py (not committed).

Exercises: adding items, sorting the menu, filtering by category,
computing an order total, and the real-user check.
"""

from models import Customer, MenuItem, Menu, Order

# --- Build a menu (adding items) ---
burger = MenuItem("Spicy Burger", 8.50, "Mains", 4.7)
soda = MenuItem("Large Soda", 2.25, "Drinks", 3.9)
cookie = MenuItem("Choc Cookie", 1.75, "Desserts", 4.9)
water = MenuItem("Water", 0.00, "Drinks", 2.1)

menu = Menu()
for item in (burger, soda, cookie, water):
    menu.add_item(item)

print("All items:", [i.name for i in menu.items])

# --- Sorting by popularity (most popular first) ---
ranked = menu.sort_by_popularity()
print("By popularity:", [(i.name, i.popularity_rating) for i in ranked])
assert [i.name for i in ranked] == ["Choc Cookie", "Spicy Burger", "Large Soda", "Water"]

# --- Filtering by category (case-insensitive) ---
drinks = menu.filter_by_category("drinks")
print("Drinks:", [i.name for i in drinks])
assert {i.name for i in drinks} == {"Large Soda", "Water"}

# --- Order total ---
order = Order()
order.add_item(burger)
order.add_item(soda)
print("Order total:", order.total_cost())
assert order.total_cost() == 10.75
assert Order().total_cost() == 0  # empty order

# --- Real-user verification ---
alice = Customer("Alice")
print("Alice real before order?", alice.is_real_user())
assert alice.is_real_user() is False
alice.add_to_history(order)
print("Alice real after order? ", alice.is_real_user())
assert alice.is_real_user() is True

print("\nOK - every method behaves as expected.")
