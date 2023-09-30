# class Solution: 
#     def is_there_most_common(self, arr, k):
#         dict = {}
#         is_k_most_common = "NO"
#         for num in arr:
#             if num not in dict:
#                 dict[num] = 1
#             else:
#                 dict[num] += 1
#         print(dict)
        
#         if k in dict:
#             count_of_k = dict[k]
#             for each_num in dict:
#                 if dict[each_num] >  count_of_k:
#                     is_k_most_common = "NO"
#                     print(is_k_most_common)
#                     return
                    
#                 else:
#                     is_k_most_common = "YES"
                
                
#         print(is_k_most_common)


    

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        lst = map(int, input().split())

        if k in lst:
            print("YES")
        else:
            print("NO")
