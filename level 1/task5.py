def is_palindrome_number(n):
    return str(n) == str(n)[::-1]
n=input("please enter the phase or word: ")
if is_palindrome_number(n):
    print(f"this word is a polindrome {n}")
else:
    print(f"this word is not a polindrome {n}")
