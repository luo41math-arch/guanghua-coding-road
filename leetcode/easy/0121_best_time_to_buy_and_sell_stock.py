def max_profit(prices):
    min_price = prices[0]
    best_profit = 0

    for price in prices:
        today_profit = price - min_price
        if today_profit > best_profit:
            best_profit = today_profit
        if price < min_price:
            min_price = price

    return best_profit

prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))