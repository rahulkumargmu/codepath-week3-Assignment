# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions

When helping with this project, follow these ground rules:

1. **Stay within the four core classes:** `Customer`, `MenuItem`, `Menu`, and
   `Order`. Do not invent new classes (no `User`, `Payment`, `Database`,
   `RecommendationEngine`, `Category`, etc.) unless I explicitly ask.
2. **Only model what the spec describes.** Each class should carry just the
   attributes named in the feature request:
   - `Customer` → `name`, `purchase_history`
   - `MenuItem` → `name`, `price`, `category`, `popularity_rating`
   - `Menu` → `items`
   - `Order` → `items`
   Do not add fields like `email`, `id`, `status`, `calories`, or `image_url`.
3. **Keep it simple.** Plain Python classes only — no inheritance, no design
   patterns, no decorators, no external libraries. Favor readable, beginner-
   friendly code over clever code.
4. **No auth, no persistence, no networking.** Skip login/passwords, databases,
   APIs, and payment processing entirely (see Project Scope above).
5. **Limit methods to the behavior the spec asks for:** verifying a real user,
   filtering the menu by category, and computing an order's total cost. Simple
   add/list helpers are fine; anything beyond that, ask first.
6. **Structure suggestions clearly:** use type hints and a one-line docstring per
   class/method, and explain *why* before showing a large change.
7. **When a request is ambiguous, ask a clarifying question** instead of
   assuming and expanding scope.
