def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # Write your solution here.
    # Print an array where each position holds the product of every other
    # element, without using division, space-separated.
    pro = 1
    l_pro = [0] * n

    for i in range(n):
        l_pro[i] = pro
        pro = pro * nums[i]

    pro = 1
    r_pro = [0] * n

    for i in range(n-1, -1, -1):
        r_pro[i] = pro
        pro = pro * nums[i]

    for i in range(n):
        print(l_pro[i] * r_pro[i], end= " ") 


if __name__ == "__main__":
    main()
