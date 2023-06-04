def main():

    name = input("What's your name? ")
    name = name.strip().title()
    hello(name)


def hello(to="world"):
    print("Hello,", to)


main()

# Start @ 4:08
