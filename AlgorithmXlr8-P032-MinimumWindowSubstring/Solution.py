def main():
    s = input().strip()
    t = input().strip()

    # Write your solution here.
    # Print the smallest substring of s that contains every character of t
    # (including duplicates), or an empty line if no such substring exists.

    n = len(s)

    freq = {}
    for ch in t:
        freq[ch] = freq.get(ch, 0) + 1

    ans_len = float('inf')
    ans = ""

    left = 0
    curr = {}
    for right in range(n):    
        ch = s[right]
        if freq.get(ch):
            curr[ch] = curr.get(ch, 0) + 1
            while not freq.get(s[left]) or curr[ch] > freq[ch]:
                el = s[left]
                if freq.get(el):
                    curr[el] -= 1
                    if curr[el] == 0:
                        curr.pop(el, None)
                left += 1
        
            if curr == freq:
                curr_len = right - left + 1
                if curr_len < ans_len:
                    ans_len = curr_len
                    ans = s[left:right+1]

    print(ans)

if __name__ == "__main__":
    main()
