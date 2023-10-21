if __name__== "__main__":

    n, m = map(int, input().split())
    flag = 1
    for i in range(n): 
        if i % 2 == 0:
            for j in range(m):
                print('#', end='')
        

     
        else:
            
            if flag == 0:
                print("#", end='')
                for j in range(1,m):
                    print(".", end="")
                    flag = 1

            else:
                for j in range(m-1):
                    print(".", end = "")
                print("#", end = '')
                flag  = 0
            
        print()
                


