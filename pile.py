t = int(input())
for i in range(t):
    j = 0
    n = int(input())
    list1 = input().split()
    list2 = list(map(int, list1))
    while j < n:
        if (max(list2) == list2[0]) or (max(list2) == list2[-1]):
            list2.remove(max(list2))
            j += 1
        else:
            break
    if j == n:
        print("Yes")
    elif j < n:
        print("No")