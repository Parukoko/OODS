print("*** New Range ***")
n = list(map(float, input("Enter Input : ").split(' ')))

def test(*args):
    lst = []
    if len(args) == 1:
        i = 0.0
        while i < args[0]:
            lst.append(round(i, 6))
            i += 1.0
    elif len(args) == 2:
        start = args[0]
        while start < args[1]:
            lst.append(round(start, 6))
            start += 1.0
    elif len(args) == 3:
        start = args[0]
        step = args[2]
        while start < args[1]:
            lst.append(round(start, 6)) 
            start += step
    return lst

lst = test(*n)
print(tuple(lst))
