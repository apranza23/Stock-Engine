import heapq
import random

class TradingEngine:
    def __init__(self):
        self.order_list={}

    def addOrder(self, order_type, ticker_symbol, stock_quantity, stock_price):
        if ticker_symbol not in self.order_list:
            self.order_list[ticker_symbol]={"BUY":[], "SELL":[]}

        order_book=self.order_list[ticker_symbol]

        if order_type == "BUY":
            while order_book["SELL"] and order_book["SELL"][0][0] <= stock_price and stock_quantity > 0:
                sell_price, sell_quantity = heapq.heappop(order_book["SELL"])
                if sell_quantity > stock_quantity:
                    print(f"Buy matched {ticker_symbol} {stock_quantity} @ {sell_price}")
                    heapq.heappush(order_book["SELL"], (sell_price, sell_quantity - stock_quantity))
                    stock_quantity = 0
                else:
                    print(f"Buy matched {ticker_symbol} {sell_quantity} @ {sell_price}")
                    stock_quantity -= sell_quantity

            if stock_quantity > 0:
                print(f"Added buy: {ticker_symbol} {stock_quantity} @ {stock_price}")
                heapq.heappush(order_book["BUY"], (-stock_price, stock_quantity)) #highest price first

        else: #When order_type is SELL
            while order_book["BUY"] and -order_book["BUY"][0][0] >= stock_price and stock_quantity > 0:
                buy_price, buy_quantity = heapq.heappop(order_book["BUY"])
                buy_price = -buy_price #converts price back to positive

                if buy_quantity > stock_quantity:
                    print(f"Sell matched {ticker_symbol} {stock_quantity} @ {buy_price}")
                    heapq.heappush(order_book["BUY"], (-buy_price, buy_quantity - stock_quantity))
                    stock_quantity = 0
                else:
                    print(f"Sell matched {ticker_symbol} {buy_quantity} @ {buy_price}")
                    stock_quantity -= buy_quantity

            if stock_quantity > 0:
                print(f"Added sell: {ticker_symbol} {stock_quantity} @ {stock_price}")
                heapq.heappush(order_book["SELL"], (stock_price, stock_quantity)) #lowest price first

def order_simulate(trading_engine, num_orders = 10):
    ticker_list = [f"STK{i+1}" for i in range(1024)]

    for _ in range(num_orders):
        order_type = random.choice(["BUY", "SELL"])
        ticker_symbol = random.choice(ticker_list)
        stock_quantity = random.randint(1,100)
        stock_price = round(random.uniform(10, 100), 2)

        trading_engine.addOrder(order_type, ticker_symbol, stock_quantity, stock_price)


if __name__ == "__main__":
    trade_engine = TradingEngine()
    order_simulate(trade_engine, 50)

