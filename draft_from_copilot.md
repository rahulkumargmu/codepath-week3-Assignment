# Draft UML — from standard chat (no reference file)

> ⚠️ This is the **first, un-bounded draft**. It was generated from a plain chat
> prompt with no project guardrails. Notice the scope creep: it invents classes
> and attributes the feature request never asked for. Kept here only so we can
> compare it against the refined design.

```mermaid
classDiagram
    class Customer {
        +int customer_id
        +str name
        +str email
        +str phone
        +str address
        +str password_hash
        +int loyalty_points
        +list~Order~ purchase_history
        +login(password) bool
        +logout() void
        +is_authenticated() bool
        +add_loyalty_points(amount) void
    }

    class MenuItem {
        +int item_id
        +str name
        +float price
        +str category
        +float popularity_rating
        +str description
        +str image_url
        +list~str~ ingredients
        +int calories
        +bool is_available
        +float discount
        +apply_discount(pct) void
    }

    class Menu {
        +list~MenuItem~ items
        +add_item(item) void
        +remove_item(item) void
        +filter_by_category(category) list~MenuItem~
        +search(query) list~MenuItem~
        +sort_by_popularity() list~MenuItem~
    }

    class Order {
        +int order_id
        +list~MenuItem~ items
        +Customer customer
        +str status
        +datetime created_at
        +add_item(item) void
        +remove_item(item) void
        +total_cost() float
        +apply_coupon(code) void
    }

    class User {
        +str username
        +str password_hash
        +str role
        +authenticate() bool
    }

    class Payment {
        +float amount
        +str method
        +str status
        +process_payment() bool
        +refund() bool
    }

    class Database {
        +connect() void
        +save(obj) void
        +load(id) object
        +query(sql) list
    }

    class RecommendationEngine {
        +recommend(customer) list~MenuItem~
        +pair_with(item) MenuItem
    }

    Customer "1" --> "many" Order : places
    Customer --|> User : extends
    Order "1" o-- "many" MenuItem : contains
    Menu "1" *-- "many" MenuItem : holds
    Order "1" --> "1" Payment : paid by
    Database ..> Customer : persists
    Database ..> Order : persists
    RecommendationEngine ..> Customer : uses
```

## What's wrong with this draft (review notes)

- **Adds classes the spec never mentions:** `User`, `Payment`, `Database`,
  `RecommendationEngine`. The request is for four core data objects only.
- **Adds authentication:** `password_hash`, `login()`, `is_authenticated()`,
  `authenticate()` — the reference file explicitly excludes auth.
- **Adds a persistence layer:** `Database` with `connect/save/load/query` — no
  database was requested.
- **Over-stuffs attributes:** `email`, `phone`, `address`, `loyalty_points`,
  `calories`, `ingredients`, `image_url`, `discount`, `order_id`, `status`,
  `created_at` — none of these appear in the feature request.
- **Invents relationships:** `Customer --|> User` inheritance, payment links, DB
  dependencies — all noise relative to what was asked.

➡️ These notes drive the cleanup in `bytebites_design.md`.
