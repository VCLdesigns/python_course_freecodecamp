def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
""" 
    if x % 2 == 0:
        return True
    else:
        return False

#Improved version
return True if n % 2 == 0 else False
"""

#Improved version
return n % 2 == 0


main()
