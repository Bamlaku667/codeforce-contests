import random 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a1 = random.randint(3, 10**9)
        a2 = random.randint(a1+1, 10**9 )
        arr = [a1, a2]
        
        i = 2
        
        while i < n:
            current = arr[-1] + 1
            while (3 * current) % (arr[i-1] + arr[i -2]) == 0 or current <= arr[i -1]:
                current += 1
                
            arr.append(current)
            
            i += 1
            
        for num in arr:
            print(num , end = " ")
            
            



