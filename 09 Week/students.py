import csv

def main():
    NUMBER_INDEX = 0
    students_dict = read_dict("students.csv", NUMBER_INDEX)
    while True:
        try:
            I_Number = input("Please enter an I-Number (xxxxxxxxx):")
            student = students_dict[I_Number]
            break
        except:
            print("No such student")
    student_name = student[1]
    print(student_name)

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    csv_dict = {}
    with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    csv_dict[key] = row_list
    return csv_dict

main()