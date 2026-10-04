def main():
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the minimal length of a contiguous subarray whose sum is at
    # least target, or 0 if no such subarray exists.

    left = 0
    curr = 0
    ans = float('inf')
    for right in range(n):
        curr += nums[right]

        while curr >= target:
            ans = min(ans, right-left+1)
            curr -= nums[left]
            left += 1
    if (ans == float('inf')): ans = 0
    print(ans)

if __name__ == "__main__":
    main()
