def is_teacher_suspicious(n, tasks):
    last_task = ""
    dict = {}
    
    for task in tasks:
        if task != last_task:
            if task in dict:
                return "NO"
            last_task = task
        if task in dict:
            dict[task] += 1
        else:
            dict[task] = 0
        
    
    return "YES"

if __name__ == "__main__":
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        tasks = input()
        result = is_teacher_suspicious(n, tasks)
        results.append(result)

    for result in results:
        print(result)