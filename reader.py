import csv


def file_read(file_name):
    with open(file_name, "r") as csvfile:
        display_file= csv.reader(csvfile)
        for item in display_file:
            print(item)


def header_row(csv_file):
    with open(csv_file, "r") as file:
        read_file = csv.reader(file)
        for row in read_file:
            return row


def get_file_contents(file_name):
    csv_list = []
    with open(file_name, "r") as file:
        read_file = csv.reader(file)
        for row in read_file:
            csv_list.append(row)
    return csv_list
