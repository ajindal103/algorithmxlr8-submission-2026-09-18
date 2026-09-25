def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print every unique triplet that sums to 0, one per line, each triplet's
    # three values space-separated in ascending order, triplets themselves
    # in ascending order. Print nothing if no triplet exists.

    nums.sort()
    ans = []
    
    for i in range(n):
        if (i != 0 and nums[i] == nums[i-1]):
            continue

        j = i+1
        k = n-1

        while (j < k):
            if (nums[i] + nums[j] + nums[k] > 0):
                k -= 1
            elif (nums[i] + nums[j] + nums[k] < 0):
                j += 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while (j < k and nums[j] == nums[j-1]):
                    j += 1
                while (j < k and nums[k] == nums[k+1]):
                    k -= 1
    
    for a, b, c in ans:
        print(a, b, c)


if __name__ == "__main__":
    main()
