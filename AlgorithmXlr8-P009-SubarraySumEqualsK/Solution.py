def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the total number of contiguous subarrays whose sum equals k.

    mp = {}
    sum = 0
    count = 0
    for i in nums:
        sum += i

        if (sum == k):
            count += 1

        x = mp.get(sum - k)
        if (x):
            count += x
            
        mp[sum] = mp.get(sum, 0) + 1

    print(count)

if __name__ == "__main__":
    main()
