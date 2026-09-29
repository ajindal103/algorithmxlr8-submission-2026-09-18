def main():
    s1 = input().strip()
    s2 = input().strip()

    # Write your solution here.
    # Print "true" if s2 contains a permutation of s1 as a substring,
    # otherwise print "false".

    def func(s1, s2):
        n = len(s1)
        m = len(s2)

        if (n > m): return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        left = 0
        for right in range(m):
            s2_count[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 == n:
                if s2_count == s1_count:
                    return True

                s2_count[ord(s2[left]) - ord('a')] -= 1
                left += 1

        return False

    print('true') if func(s1, s2) else print('false')

if __name__ == "__main__":
    main()
