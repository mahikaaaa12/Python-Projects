def palindrome(lst):
    for i in lst:
        if i==i[::-1]:
            return i
lst=eval(input("Enter a list of strings:"))
print("The palindrome strings are:",palindrome(lst))
