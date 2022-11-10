def popit(list, location):
    list.pop(location)

def ammendit(list, value):
    list.append(value)

def changeit(list, location, value):
    list[location] = value

def main():
    list = []
    ammendit(list, "list")
    changeit(list, 0, "beans")
    ammendit(list, "greens")
    popit(list, 0)
    changeit(list, 0, "more beans")
    print(list)

main()