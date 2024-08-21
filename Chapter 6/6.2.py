def palindrome(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[:mid] == s[mid:][::-1]
    else:
        return s[:mid] == s[mid+1:][::-1]

str_input = input("Enter Input : ")
if palindrome(str_input):
    print(f"'{str_input}' is palindrome")
else:
    print(f"'{str_input}' is not palindrome")
