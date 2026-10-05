def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum number of consecutive 1s achievable after
    # flipping at most k zeros to ones.

    left = 0
    ans = 0

    for right in range(n):
        if nums[right] == 0:
            k -= 1

        while k < 0 and left < right:
            k += 1 if nums[left] == 0 else 0
            left += 1

        ans = max(ans, right - left + 1)

    print(ans)

if __name__ == "__main__":
    main()
