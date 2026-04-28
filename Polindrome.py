#polindrome for String

def isPalindrome(name):
    if name==name[::-1]:
        print(name, "is a polindrome")
    else:
        print(name, "is not a polindrome")
    return""
print(isPalindrome("madam"))
print(isPalindrome("subaash"))

#polindrome for Integer
def isPalindrome(name):
    if str(name)==str(name[::-1]):
        print(name, "is a polindrome")
    else:
        print(name, "is not a polindrome")
    return""

print(isPalindrome("1221"))