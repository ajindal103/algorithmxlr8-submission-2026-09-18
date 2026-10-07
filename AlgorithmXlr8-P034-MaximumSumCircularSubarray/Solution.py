def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum possible sum of a non-empty subarray of the
    # circular array nums (wraparound from the end to the start allowed).

    total_sum = 0
    curr_min_sum = float('inf')
    curr_max_sum = float('-inf')
    best_min_sum = float('inf')
    best_max_sum = float('-inf')

    for i in nums:
        curr_min_sum = min(i, i + curr_min_sum)
        curr_max_sum = max(i, i + curr_max_sum)
        best_min_sum = min(curr_min_sum, best_min_sum)
        best_max_sum = max(curr_max_sum, best_max_sum)
        total_sum += i

    if best_max_sum < 0:
        print(best_max_sum)
    else:
        print(max(total_sum - best_min_sum, best_max_sum))

if __name__ == "__main__":
    main()
