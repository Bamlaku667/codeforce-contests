def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        given_str = input()
        
        num_of_operations = 0
        i = 0

        while i< len(given_str):
            while i < len(given_str) and given_str[i] == 'W':
                i+= 1

            if i < len(given_str):
                num_of_operations += 1
                i+= k
        print(num_of_operations)

if __name__ == "__main__":
    main()