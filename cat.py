""" 
print("meow")
print("meow")
print("meow")

# Improved Code
i = 0
while i < 3:
    print("Meow!")
    i += 1

# Improved Code
for _ in range(3):
    print("Meow!")

# Alternate Code
print("Meow!\n" * 3, end="")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow!")
"""


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("Meow!")


main()
