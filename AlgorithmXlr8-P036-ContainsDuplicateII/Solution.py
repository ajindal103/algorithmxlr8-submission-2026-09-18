def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print "true" if two equal values exist within index distance k of each
    # other, otherwise print "false".

    mp = {}
    ans = False
    for i in range(n):
        if nums[i] in mp and i - mp[nums[i]] <= k:
            ans = True
            break
        mp[nums[i]] = i

    print("true") if ans else print("false")       

if __name__ == "__main__":
    main()
