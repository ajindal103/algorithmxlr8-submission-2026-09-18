def main():
    n = int(input())
    prices = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum profit achievable from a single buy followed by a
    # single later sell, or 0 if no profit is possible.
    buy = prices[0]
    maxp = 0

    for i in range(1, n):
        buy = min(buy, prices[i])
        profit = prices[i] - buy
        maxp = max(maxp, profit)

    print(maxp)


if __name__ == "__main__":
    main()
