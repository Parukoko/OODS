lst = []

def insertion(inp, n):
    if len(inp) <= 0:
        return
    curr = inp.pop(0)
    if len(inp) == n - 1:
        lst.append(curr)
    elif not lst or curr > lst[-1]:
        lst.append(curr)
        print(f"insert {curr} at index {len(lst)-1} : {lst}", end=" ")
        if inp:
            print(inp)
        else:
            print()
    else:
        insert(lst, curr, len(lst)-1, inp)
    insertion(inp, n)

def insert(lst, curr, i, inp):
    if i < 0:
        lst.insert(0, curr)
        print(f"insert {curr} at index 0 : {lst}", end=" ")
        if inp:
            print(inp)
        else:
            print()
        return
    elif curr > lst[i]:
        lst.insert(i+1, curr)
        print(f"insert {curr} at index {i+1} : {lst}", end=" ")
        if inp:
            print(inp)
        else:
            print()
        return
    else:
        insert(lst, curr, i-1, inp)

inp = list(map(int, input("Enter Input : ").split()))
n = len(inp)
insertion(inp, n=n)
print("sorted")
print(lst)
