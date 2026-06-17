"""ByteBites backend models.

Four core classes (see bytebites_design.md):

1. Customer  - a real app user; stores `name` and `purchase_history`,
               and can verify it is a genuine user.
2. MenuItem  - one sellable food item; stores `name`, `price`,
               `category`, and `popularity_rating`.
3. Menu      - the full collection of MenuItems; can filter by category
               and sort by popularity.
4. Order     - a single transaction; stores selected items and computes
               the total cost.
"""

from __future__ import annotations


class MenuItem:
    """A single sellable food item on the ByteBites menu."""

    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        popularity_rating: float,
    ) -> None:
        self.name: str = name
        self.price: float = price
        self.category: str = category
        self.popularity_rating: float = popularity_rating


class Menu:
    """The full collection of MenuItems, filterable by category."""

    def __init__(self) -> None:
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add a MenuItem to the menu's collection."""
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[MenuItem]:
        """Return all items in the given category (e.g. "Drinks").

        The match is case-insensitive so "drinks" and "Drinks" agree.
        """
        return [
            item
            for item in self.items
            if item.category.lower() == category.lower()
        ]

    def sort_by_popularity(self) -> list[MenuItem]:
        """Return the items most-popular-first, without mutating the menu."""
        return sorted(
            self.items,
            key=lambda item: item.popularity_rating,
            reverse=True,
        )


class Order:
    """A single transaction: the items a user selected plus their total."""

    def __init__(self) -> None:
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add a selected MenuItem to this order."""
        self.items.append(item)

    def total_cost(self) -> float:
        """Return the combined price of every item in the order (0 if empty)."""
        return sum(item.price for item in self.items)


class Customer:
    """A real ByteBites user, identified by name and past orders."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.purchase_history: list[Order] = []

    def add_to_history(self, order: Order) -> None:
        """Record a completed order in this customer's history."""
        self.purchase_history.append(order)

    def is_real_user(self) -> bool:
        """Return True if the customer has a name and at least one past order.

        The spec verifies "real users" by name + past purchase history, so a
        customer with no orders is treated as unverified.
        """
        return bool(self.name) and len(self.purchase_history) > 0
