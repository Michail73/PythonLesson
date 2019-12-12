# function which return reverse of a string
def reverse(string):
    return string[::-1]


def isPalindrome(stirng):
    # Calling reverse function
    rev = reverse(string)

    # Checking if both string are equal or not
    if (string== rev):
        return True
    return False


# Driver code
print("'Pls input digit to check if it is palindrom or not'\n")
string = str(input())
ans = isPalindrome(string)

if ans == 1:
    print("Yes")
else:
    print("No")