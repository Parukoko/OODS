print("*** Fun with Drawing ***")
print("Enter input : ", end='')
n = int(input())
if n < 2:
    exit()
elif n == 2:
    print('.' * (n-1), end='')
    print('*', end='')
    print('.' * ((n-1) * 2 - 1), end='')
    print('*', end='')
    print('.' * (n-1), end='\n')

    # --------second----------
    for i in range(n-1):
        print('.' * (n-i-2), end='')
        print('*', end='')
        print('+' * (i * 2 + 1), end='')
        print('*', end='')
        print('+' * (i * 2 + 1), end='')
        print('*', end='')
        print('.' * (n-i-2), end='\n')

    # --------half----------
    for i in range((n*2) - 3):
        print("." * (i+1), end='')
        print('*', end='')
        print('+', end='')
        print('*', end='')
        print("." * (i+1), end='\n')

    #  --------last----------
    print('.' * (n*2 - 2), end='')
    print('*', end='')
    print('.' * (n*2 - 2), end='')
else:
    # --------first----------
    print('.' * (n-1), end='')
    print('*', end='')
    print('.' * ((n-1) * 2 - 1), end='')
    print('*', end='')
    print('.' * (n-1), end='\n')

    # --------second----------
    for i in range(n-2):
        print('.' * (n-i-2), end='')
        print('*', end='')
        print('+' * (i * 2 + 1), end='')
        print('*', end='')
        print('.' * ((n-i) * 2 - 5), end='')
        print('*', end='')
        print('+' * (i * 2 + 1), end='')
        print('*', end='')
        print('.' * (n-i-2), end='\n')
    # --------half----------
    print('*', end='')
    print('+' * (n*2-3), end='')
    print('*', end='')
    print('+' * (n*2-3), end='')
    print('*', end='\n')

    # --------half----------
    for i in range((n*2) - 3):
        print("." * (i+1), end='')
        print('*', end='')
        print('+' * ((n*2 - i) * 2 - 7), end='')
        print('*', end='')
        print("." * (i+1), end='\n')

    #  --------last----------
    print('.' * (n*2 - 2), end='')
    print('*', end='')
    print('.' * (n*2 - 2), end='')
