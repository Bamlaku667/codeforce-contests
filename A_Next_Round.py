if __name__ == "__main__":
    n, k = map(int, input().split())
    lst  = [int(num) for num in input().split()]

    if k < 0 or k > n:
        print('invalid') 
    else:
        count = 0
        position = lst[k]
        for num in lst:
            if num >= position and num > 0:
                count += 1
        print(count)