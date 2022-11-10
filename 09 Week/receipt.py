import csv

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

def main():
    key_column_index = 0
    products_dict = read_dict("products.csv", key_column_index)
    print(products_dict)
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            quantity = row_list[1]
            item = row_list[0]
            item_info = products_dict[item]
            print(f"{item_info[1]}: {quantity} @ {item_info[2]}")



main()
