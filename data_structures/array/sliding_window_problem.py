# sliding window problems 
from turtle import left, right


chocolate = [2, 4, 6, 1, 7, 3, 5]

def sliding_window(prices, window_size):
    if window_size > len(prices):
        return []

    max_sum = 0
    current_sum = sum(prices[:window_size])
    max_sum = current_sum

    for i in range(window_size, len(prices)):
        current_sum += prices[i] - prices[i - window_size]
        max_sum = max(max_sum, current_sum)

    return max_sum

result = sliding_window(chocolate, 3)
print(f"The maximum sum of {3} consecutive elements in the array is: {result}")
    

        