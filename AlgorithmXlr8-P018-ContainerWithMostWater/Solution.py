def main():
    n = int(input())
    height = list(map(int, input().split()))

    # Write your solution here.
    # Print the maximum amount of water that can be contained between any
    # two lines of height.

    i = 0
    j = n-1

    ans = 0
    while (i<j):
        ans = max(ans, (j-i)*(min(height[i], height[j])))

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    
    print(ans)


if __name__ == "__main__":
    main()
