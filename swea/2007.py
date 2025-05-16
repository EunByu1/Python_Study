T = int(input())

for i in range(1, T+1):
    string = input().rstrip()
    check = list(set(string))
    
    for j in range(1, 10):
        if string[:j] == string[j:j*2]:
            # all(word in list/string for word in keywords
            if all(word in string[:j] for word in check):
                print(f"#{i}", end=" ")
                print(len(string[:j]))
                break
