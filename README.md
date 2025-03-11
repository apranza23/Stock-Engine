Features

Order Matching: Matches buy and sell orders based on price and quantity.

Order Book Management: Maintains separate buy and sell order books.

Efficient Processing: Uses priority queues (heaps) for optimized trade execution.

Simulation Support: Generates random trade orders for testing purposes.

Code Overview

addOrder.py

Implements the TradingEngine class.

Handles adding and matching buy/sell orders.

Uses heaps to maintain order books efficiently.

Contains order_simulate() to generate random stock orders.

matchOrder.py

Defines the Order class.

Implements the matchOrder() function to match buy and sell orders.

Processes orders based on price and quantity.

Requirements

Python 3.8+

heapq, random
