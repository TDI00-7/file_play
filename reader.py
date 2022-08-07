import csv

def file_read(file_name):
    with open(file_name, mode = "r") as csvfile:
        display_file= csv.reader(csvfile)
        
        for item in display_file:
            print(item)

