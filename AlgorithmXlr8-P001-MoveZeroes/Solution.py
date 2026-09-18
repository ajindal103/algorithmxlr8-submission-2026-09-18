def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print nums after moving all zeroes to the end, preserving the
    # relative order of the non-zero elements, space-separated.

    i = 0
    j = 0

    while (j<n):
        if (nums[j] == 0): 
            j += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    for x in range(0, n):
        print(nums[x], end = " ")


if __name__ == "__main__":
    main()
