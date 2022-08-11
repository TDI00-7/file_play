import csv

def file_read(file_name):
    with open(file_name, mode = "r") as csvfile:
        display_file= csv.reader(csvfile)
        
        for item in display_file:
            print(item)
    
        csvfile.close

def header_row(csv_file):
    csv_list = []
    with open(csv_file, "r") as file:
        read_file = csv.reader(file)
        for row in read_file:
            csv_list.append(row)
        file.close
        return csv_list[0]