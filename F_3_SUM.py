

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = [int(num) for num in input().split()]
        nums.sort()
        is_find = False
        
        right = n -1 
        for i in range(n -2):
            left = i+ 1
            while (left < right):
                sum_of_nums  = nums[i] + nums[left] + nums[right]
                if str(sum_of_nums)[-1] == '3':
                    is_find = True
                    break
                elif sum_of_nums > 3:
                    right -= 1
                else: 
                    left += 1


            if is_find:
                
                break
        
        if is_find:
            print("YES")

        else:
            print("NO")