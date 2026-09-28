def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum average of any length-k contiguous subarray,
    # formatted to exactly 5 decimal places.

    left, right = 0, 0
    sum, maxi = 0, float('-inf')
    for right in range(n):
        sum += nums[right]

        if right - left + 1 == k:
            maxi = max(maxi, sum)
            sum -= nums[left]
            left += 1

    print(f"{(maxi/k):,.5f}")


if __name__ == "__main__":
    main()
