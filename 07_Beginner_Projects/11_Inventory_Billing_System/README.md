# Project: Inventory and Billing System

## What this project does

Create a bill from a sample product catalogue, check stock and calculate 5% demo tax.

## Python concepts used

Nested dictionaries, loops, cart totals, input validation, arithmetic and formatted strings.

## How it works, step by step

1. Display product IDs, prices and stock.
2. Add valid product quantities to a cart without exceeding available stock.
3. Calculate each line total and the subtotal.
4. Add 5% sample tax and show the grand total.
5. Decrease stock after a non-empty bill is completed.

## Files used

- `main.py` — Inventory catalogue, cart, billing and stock checks.

## How to run

1. Install Python 3.
2. Open this project folder in a terminal.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Learning note

Products and stock are held in memory, so stock resets when the program exits. This keeps the starter project simple.

After the first run, change some inputs and explain how the code uses each listed concept.
