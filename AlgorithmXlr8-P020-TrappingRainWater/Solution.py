def main():
    n = int(input())
    height = list(map(int, input().split()))

    # Write your solution here.
    # Print the total amount of water trapped between the bars of height.

    left = [0] * n
    right = [0] * n

    curr = 0
    for i in range(n):
        left[i] = curr
        curr = max(curr, height[i])

    curr = 0
    for i in range(n-1, -1, -1):
        right[i] = curr
        curr = max(curr, height[i])

    ans = 0
    for i in range(n):
        ans += max(0, min(left[i], right[i]) - height[i])

    print(ans)

if __name__ == "__main__":
    main()
