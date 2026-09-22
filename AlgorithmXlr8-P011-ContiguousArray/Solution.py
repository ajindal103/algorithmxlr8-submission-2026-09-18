def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum length of a contiguous subarray with an equal
    # number of 0s and 1s.

    # This function finds the longest continuous part of the list that has equal numbers of 0s and 1s.
    # It keeps a running sum to measure the balance between 1s and 0s as it moves through the list.
    # Every 1 increases the running sum by 1, and every 0 decreases it by 1.
    # If the same running sum appears again, the section between those two positions is balanced.
    # That works because the extra gain and loss between those positions cancel each other out.
    # The dictionary saves the first position where each running sum was seen.
    # It begins with sum 0 at position -1 so a balanced section starting from index 0 can be counted.
    # Each time a repeated running sum is found, the code calculates the length of that balanced section.
    # The function keeps track of the largest balanced length seen so far.
    # For the input [0, 1, 0, 1], the whole list is balanced, so the answer is 4.

    total = 0
    mp = {0: -1}
    ans = 0

    for i in range(n):
        total += (1 if nums[i]==1 else -1)

        if mp.get(total):
            ans = max(ans, i - mp[total])
        else:
            mp[total] = i

    print(ans)


if __name__ == "__main__":
    main()
