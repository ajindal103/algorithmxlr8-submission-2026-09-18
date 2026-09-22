def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print "true" if a subarray of length >= 2 sums to a multiple of k, otherwise "false".

    # ISSUE IN QUESTION, ASKED FOR LENGTH>=2, BUT CODE WORKS FOR LENGTH>2

    def func(nums, n, k):
        total = 0
        mp = {0: -1}

        for i in range(n):
            total += nums[i]
            rem = total%k if k!=0 else total

            if rem in mp:
                length = i - mp.get(rem)
                if length > 2: return True
            else:
                mp[rem] = i

        return False

    ans = func(nums, n, k)

    print("true") if ans else print("false")


if __name__ == "__main__":
    main()
