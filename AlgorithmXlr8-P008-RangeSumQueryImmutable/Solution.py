def main():
    n = int(input())
    nums = list(map(int, input().split()))
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    # Write your solution here.
    # Precompute a prefix sum array once, then for each query (left, right),
    # print sum(nums[left..right]) (inclusive) on its own line.

    prefix = [0] * n
    prefix[0] = nums[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + nums[i]

    for s, e in queries:
        if s == 0:
            x = 0
        else:
            x = prefix[s-1]
        print(prefix[e] - x)


if __name__ == "__main__":
    main()
