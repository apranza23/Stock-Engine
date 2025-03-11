class Order:
    def __init__(self, stock_price, stock_quantity, order_type):
        self.stock_price = stock_price
        self.stock_quantity = stock_quantity
        self.order_type = order_type

def matchOrder(buy_orders, sell_orders):
    buy_orders.sort(key=lambda x: x.stock_price, reverse = True)
    sell_orders.sort(key=lambda x: x.stock_price)

    matched_orders = []

    i,j = 0,0

    while i<len(buy_orders) and j<len(sell_orders):
        buy_order = buy_orders[i]
        sell_order = sell_orders[j]

        if buy_order.stock_price >= sell_order.stock_price:
            matched_orders.append((buy_order, sell_order))
            buy_order.stock_quantity -= sell_order.stock_quantity
            sell_order.stock_quantity -= sell_order.stock_quantity

            if buy_order.stock_quantity == 0:
                i += 1

            if sell_order.stock_quantity == 0:
                j += 1

        else:
            break

    return matched_orders
    
buy_Order = [Order(100, 10, 'Buy'), Order(105, 20, 'Buy'), Order(98, 15, 'Buy')]
sell_Order = [Order(99, 10, 'Sell'), Order(101, 5, 'Sell'), Order(103, 15, 'Sell')]

matched = matchOrder(buy_Order, sell_Order)

for buy, sell in matched:
    print(f"Matched Buy Order: Price={buy.stock_price}, Quantity={buy.stock_quantity} with Sell Order: Price={sell.stock_price}, Quantity={sell.stock_quantity}")

                