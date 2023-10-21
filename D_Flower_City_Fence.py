def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        list_of_nums = [int(number) for number in input().split()]
        if n != list_of_nums[0]:
            print("NO")
            return 
        




if __name__ == "__main__":
    

# Example usage:
    n1 = 5
    heights1 = [5, 4, 3, 2, 1]

    n2 = 3
    heights2 = [4, 2, 1]

    print(is_symmetrical_fence(n1, heights1))  # Output: "YES"
    print(is_symmetrical_fence(n2, heights2))  # Output: "NO"
        