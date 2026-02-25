prices = [10, 1, 5, 6, 7, 1]


def maxProfit(prices):
    res = 0
    start = prices[0]
    value = 0
    for price in prices:
        if price > start:
            value += price - start
            start = price
            res = max(res, value)
        else:
            value = 0
            start = price
    return res


def windowProfit(prices):
    max_value = 0
    left = 0
    for right in range(1, len(prices)):
        if prices[right] > prices[left]:
            max_value = max(max_value, prices[right] - prices[left])
        else:
            left = right
    return max_value


print(maxProfit(prices))
print(windowProfit(prices))
