def main():
    n = int(input())
    prices = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum total profit.

    ans = 0
    buy = prices[0]

    for i in range(1, n):
        if (buy < prices[i]):
            ans += prices[i] - buy
        
        buy = prices[i]

    print(ans) 

if __name__ == "__main__":
    main()
