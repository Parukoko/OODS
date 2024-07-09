def Rshift(num, shift):
    return num >> shift

def dec2bin(number):
    if number == 0:
        return "0"
    ans = ""
    while number:
        ans += str(number & 1)
        number = number >> 1
    return ans[::-1]

n, s = map(int, input("Enter number and shiftcount : ").split())
print(Rshift(n, s))

