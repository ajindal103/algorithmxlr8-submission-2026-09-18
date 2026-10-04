def main():
    s = input().strip()
    k = int(input())

    # Write your solution here.
    # Print the length of the longest substring that can be made into a
    # single repeated letter using at most k character replacements.

    n = len(s)
    ans = 0
    left = 0
    freq = [0] * 26

    maxi = 0
    for right in range(n):
        x = ord(s[right]) - ord('A')
        freq[x] += 1
        maxi = max(maxi, freq[x])

        while ((right-left+1) - maxi) > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        ans = max(ans, right-left+1)
        
    print(ans)


if __name__ == "__main__":
    main()

# Use a sliding window to find the longest substring that can become the same character using at most k replacements.
# Keep a frequency count of each character currently inside the window.
# Expand the window by moving the right pointer one character at a time.
# Track the highest frequency of any single character inside the current window.
# The number of replacements needed is the window length minus the highest character frequency.
# If the replacements needed are greater than k, the current window is invalid.
# Shrink the window from the left until the number of required replacements becomes at most k.
# After making the window valid, calculate its current length.
# Keep track of the largest valid window length found so far.
# Continue until the right pointer reaches the end and return the largest valid length.