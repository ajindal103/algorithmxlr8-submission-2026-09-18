def main():
    s = input()

    # Write your solution here.
    # Print the length of the longest substring of s with no
    # repeating characters.

    n = len(s)
    freq = {}
    ans = 0
    left, right = 0, 0

    for right in range(n):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while(freq[s[right]] > 1):
            freq[s[left]] -= 1
            left += 1

        ans = max(ans, right-left+1)

    print(ans)

if __name__ == "__main__":
    main()
