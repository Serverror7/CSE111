import json
def create_new_person_data():
    family_data = []
    users = 0
    while users >= 0:
        name = input("Name: ")
        age = input("Age: ")
        entry = {"Name":name,"Age":age}
        family_data.append(entry)
        add_another = input("Would you like to add another family member? (Y/N) ")
        if add_another != "Y":
            users = users - 1

def add_new_members_to_family_data(family_data):
    with open('readme.txt', 'a') as f:
        for person in family_data:
            f.write(json.dumps(person))


def read_family_data():
    f = open('readme.txt', 'r')
    print(f.read)

def main():
    # family_data = create_new_person_data()
    # add_new_members_to_family_data(family_data)
    read_family_data()

main()