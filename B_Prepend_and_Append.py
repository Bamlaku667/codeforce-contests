if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        binary_str = input()

        if n == 1:
            print(1)
            continue

        str_list = list(binary_str)
        i = 0
        j = n-1 
        
        while (i < j):
            if str_list[i] == '0':
                if str_list[j] == '1':
                    str_list.pop(j)
                    str_list.pop(i)
                    i += 1
                    j -= 1
                else:
                    print(len(str_list))


            elif str_list[i] == '1':
                if str_list[j] == '0':
                    str_list.pop(j)
                    str_list.pop(i)
                    i += 1
                    j -= 1

                else :
                    print(len(str_list))

        
