def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print "true" if a subarray of length >= 2 sums to a multiple of k, otherwise "false".

    def check_subarray_sum(nums, k):
        seen = {0: -1}                        # remainder -> first index seen (seed: empty prefix at -1)
        total = 0
        for i, x in enumerate(nums):
            total += x
            rem = total % k if k != 0 else total
            if rem in seen:
                if i - seen[rem] > 2:              # far enough apart to have length at least 2
                    return True
            else:
                seen[rem] = i
        return False

    ans = check_subarray_sum(nums, k)

    print("true") if ans else print("false")


if __name__ == "__main__":
    main()
