def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the smallest missing positive integer, in O(n) time and O(1)
    # extra space (beyond the input array itself).

    # This solution finds the smallest positive number that does not appear in the list.

    # It first collects all the numbers into a fast lookup group, so it can quickly check whether a number exists.

    # It starts by assuming the answer might be 1.

    # It checks whether 1 is already present in the list.

    # If 1 is present, it moves to the next possible answer, which is 2.

    # It keeps increasing the candidate number one by one as long as that number is found in the list.

    # The moment it reaches a number that is not present, it stops.

    # That missing number is the smallest positive integer not in the list.

    # Negative numbers and zero do not matter here, because the task only cares about positive integers.

    # For the example list, 1 is present but 2 is missing, so the answer is 2./

    ans = 1

    mp = {}
    for num in nums:
        mp[num] = mp.get(num, 0) + 1
    
    i = 1
    while (i < n+1):
        if mp.get(i):
            i += 1
        else:
            break

    print(i)
            


if __name__ == "__main__":
    main()
