def main():
    n, target = map(int, input().split())
    numbers = list(map(int, input().split()))

    # Write your solution here.
    # Print the two 1-indexed indices (space-separated) of the numbers that
    # add up to target, index1 < index2.


    def func():
        i, j = 0, n-1
        while (i<j):
            if (numbers[i] + numbers[j] < target):
                i += 1
            elif (numbers[i] + numbers[j] > target):
                j -= 1
            else:
                return i, j

        return 0, 0

    a, b = func()
    print(a+1, b+1)


if __name__ == "__main__":
    main()
