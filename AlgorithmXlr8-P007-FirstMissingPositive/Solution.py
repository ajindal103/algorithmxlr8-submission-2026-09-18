def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the smallest missing positive integer, in O(n) time and O(1)
    # extra space (beyond the input array itself).

    # ans = 1

    # mp = {}
    # for num in nums:
    #     mp[num] = mp.get(num, 0) + 1
    
    # i = 1
    # while (i < n+1):
    #     if mp.get(i):
    #         i += 1
    #     else:
    #         break

    # print(i)

    for i in range(n):
        while (1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]):
            tar = nums[i] - 1
            nums[i], nums[tar] = nums[tar], nums[i]

    b = False
    for i in range(n):
        if (nums[i] != i+1):
            print(i+1)
            b = True
            break
      
    if not b: print(n+1)

if __name__ == "__main__":
    main()
