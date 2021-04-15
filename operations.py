
class Operations():

    def __init__(self, budget):
        self.budget = budget
        self.assets = {}
        self.buy_price = {}

    def sell(self, name, count, price):
        if name in self.assets.keys():
            if self.assets[name] == 0:
                print("No asset in estate")
            if self.assets[name] >= count:
                self.assets[name] -= count
                self.budget += count * price
            else:
                print("Selling counts more than having")
        else:
            print("No asset of this ticker")

    def buy(self, name, count, price):
        if self.budget >= price * count:
            self.budget -= price * count
            if name in self.assets.keys():
                self.assets[name] += count
                self.buy_price[name] = price
            else:
                self.buy_price.update({name: price})
                self.assets.update({name: count})
        else:
            print("No money in budget")

    def stop_loss(self, name, current_price, percentage):
        if (self.buy_price[name] - current_price) / self.buy_price[name] > percentage:
            self.sell(name, self.assets[name], current_price)

    def take_profit(self, name, current_price, percentage):
        if (current_price - self.buy_price[name]) / self.buy_price[name] > percentage:
            self.sell(name, self.assets[name], current_price)
