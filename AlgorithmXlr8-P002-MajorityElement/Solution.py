def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the element that appears more than n / 2 times.

    count = 0
    el = nums[0]

    for x in nums:
        if (x == el):
            count += 1
        else:
            count -= 1
            if (count == 0):
                el = x
                count = 1
    
    print(el)

if __name__ == "__main__":
    main()
