def main():
    n = int(input())
    strs = input().split()

    # Write your solution here.
    # Print each group of anagrams on its own line, words space-separated,
    # in the order each group's signature was first encountered while
    # scanning strs, and words within a group in their original input order.

    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        groups.setdefault(key, []).append(s)

    for value in groups.values():
        print(*value)

if __name__ == "__main__":
    main()
