def main():
    t = int(input())
    is_balaned = False
    for _ in range(t):
        n = int(input())
        given_str = input()
        if n<=1:
            print("-1 -1")
            continue

        else:
            for i in range(0, n-1):
                if given_str[i] != given_str[i+1]:
                    is_balaned = True
                    print(i+1, i+2)
                    break

                
            if is_balaned == False:
                print(-1, -1)



        
        
                
        


if __name__ == "__main__":
    main()

