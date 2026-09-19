def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print nums after rotating it to the right by k steps, space-separated.

    def swap(a, b, nums):
        if (a >= b): return

        while (a<b):
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b -= 1
    
    swap(0, n-k-1, nums)
    swap(n-k, n-1, nums)
    swap(0, n-1, nums)

    for i in nums:
        print(i, end=" ")

if __name__ == "__main__":
    main()
