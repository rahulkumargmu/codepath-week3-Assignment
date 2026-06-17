"""ByteBites backend models.

Four core classes (see bytebites_design.md):

1. Customer  - a real app user; stores `name` and `purchase_history`,
               and can verify it is a genuine user.
2. MenuItem  - one sellable food item; stores `name`, `price`,
               `category`, and `popularity_rating`.
3. Menu      - the full collection of MenuItems; can filter by category.
4. Order     - a single transaction; stores selected items and computes
               the total cost.
"""
