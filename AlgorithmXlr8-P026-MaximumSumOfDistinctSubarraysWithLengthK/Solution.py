def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum sum among length-k subarrays with no duplicate
    # elements, or 0 if none exist.

    # This function finds the largest sum of any subarray of length k where all numbers are different.
    # It uses a sliding window, which means it examines one group of k elements at a time.
    # window_sum keeps track of the total of the current window.
    # freq stores how many times each number appears inside the current window.
    # As the loop moves forward, the new number is added to both the sum and the frequency map.
    # Once the window becomes larger than k, the oldest number is removed from the sum and its count is reduced.
    # If a number’s count becomes zero, it is deleted from freq because it is no longer inside the window.
    # When len(freq) equals k, that means all k numbers in the current window are distinct.
    # At that point, the code compares the current window sum with the best answer found so far.
    # For the example input, the maximum valid sum is 15, coming from the subarray [4, 2, 9].

    freq = {}
    curr_sum = 0
    ans = 0

    left = 0
    for right in range(n):
        el = nums[right]
        curr_sum += el
        freq[el] = freq.get(el, 0) + 1

        if right - left + 1 == k:
            if (len(freq) == k):
                ans = max(ans, curr_sum)

            rem_el = nums[left]
            curr_sum -= rem_el
            freq[rem_el] -= 1
            if freq.get(rem_el) == 0:
                del freq[rem_el]
            
            left += 1

    print(ans)


if __name__ == "__main__":
    main()
