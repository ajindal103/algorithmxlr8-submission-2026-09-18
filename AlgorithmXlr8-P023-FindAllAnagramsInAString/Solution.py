def main():
    s = input().strip()
    p = input().strip()

    # Write your solution here.
    # Print every start index in s where an anagram of p begins,
    # space-separated in ascending order.

    def func(s, p):
        n = len(s)
        m = len(p) 

        if m > n:
            return []

        p_cnt, win_cnt = [0]*26, [0]*26

        for ch in p:
            p_cnt[ord(ch) - ord('a')] += 1

        result = []
        left = 0
        for right in range(n):
            win_cnt[ord(s[right]) - ord('a')] += 1

            if right - left + 1 == m:
                if win_cnt == p_cnt:
                    result.append(left)
                
                win_cnt[ord(s[left]) - ord('a')] -= 1
                left += 1

        return result

    
    ans = func(s, p)
    for i in ans:
        print(i, end=" ")


if __name__ == "__main__":
    main()
