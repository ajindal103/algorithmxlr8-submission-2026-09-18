def main():
    s = input()

    # Write your solution here.
    # Print the length of the longest substring of s with no
    # repeating characters.

    freq = {}
    ans, curr = 0, 0

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        curr += 1

        if freq[ch] > 1:
            curr = 0
            freq.clear()
        
        ans = max(curr, ans)

    print(ans)

if __name__ == "__main__":
    main()
