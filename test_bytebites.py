"""Pytest tests for the ByteBites models.

Each test describes one behavior from the spec in a single sentence and checks
the output the system produces, not how it is implemented.
"""

import pytest

from models import Customer, MenuItem, Menu, Order


@pytest.fixture
def sample_items():
    """Four menu items spanning three categories and varied popularity."""
    return {
        "burger": MenuItem("Spicy Burger", 8.50, "Mains", 4.7),
        "soda": MenuItem("Large Soda", 2.25, "Drinks", 3.9),
        "cookie": MenuItem("Choc Cookie", 1.75, "Desserts", 4.9),
        "water": MenuItem("Water", 0.00, "Drinks", 2.1),
    }


@pytest.fixture
def menu(sample_items):
    """A Menu preloaded with all of the sample items."""
    m = Menu()
    for item in sample_items.values():
        m.add_item(item)
    return m


# --- Order totals (happy path) ---

def test_order_total_with_multiple_items(sample_items):
    """Adding a $8.50 burger and a $2.25 soda totals $10.75."""
    order = Order()
    order.add_item(sample_items["burger"])
    order.add_item(sample_items["soda"])
    assert order.total_cost() == 10.75


# --- Order totals (edge case) ---

def test_order_total_is_zero_when_empty():
    """An order with no items has a total of $0, not an error."""
    assert Order().total_cost() == 0


# --- Filtering by category ---

def test_filter_by_category_returns_only_that_category(menu):
    """Filtering 'Drinks' returns only the two drink items."""
    drinks = menu.filter_by_category("Drinks")
    assert {item.name for item in drinks} == {"Large Soda", "Water"}


def test_filter_by_category_is_case_insensitive(menu):
    """Filtering 'drinks' matches the same items as 'Drinks'."""
    assert len(menu.filter_by_category("drinks")) == 2


def test_filter_by_unknown_category_returns_empty(menu):
    """Filtering a category that has no items returns an empty list."""
    assert menu.filter_by_category("Soups") == []


# --- Sorting by popularity ---

def test_sort_by_popularity_orders_high_to_low(menu):
    """Sorting lists items from highest to lowest popularity rating."""
    ranked = [item.name for item in menu.sort_by_popularity()]
    assert ranked == ["Choc Cookie", "Spicy Burger", "Large Soda", "Water"]


def test_sort_by_popularity_does_not_mutate_menu(menu):
    """Sorting returns a new list and leaves the menu's own order intact."""
    original = list(menu.items)
    menu.sort_by_popularity()
    assert menu.items == original


# --- Real-user verification ---

def test_customer_is_not_real_without_history():
    """A new customer with no past orders is not yet a verified user."""
    assert Customer("Alice").is_real_user() is False


def test_customer_is_real_after_purchase(sample_items):
    """A customer with at least one past order is a verified user."""
    alice = Customer("Alice")
    order = Order()
    order.add_item(sample_items["burger"])
    alice.add_to_history(order)
    assert alice.is_real_user() is True
