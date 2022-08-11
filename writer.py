import csv
import reader

def file_write(new_csv):

    header_row_list = str(input("Enter Header Row using (,) to seperate the columns\n").split(","))
    with open(input(new_csv), "w") as csvfile:
        ex_write = csv.writer(csvfile)
        ex_write.writerow(header_row_list)

        while True:
            user_input = input("Enter row seperated by a comma (,)\nEnter (exit) to quit\n")
            if user_input == "exit":
                break
            row = user_input.split(",")
            if len(header_row_list) == len(row):
                ex_write.writerow(row)
            else:
                print("Invalid entry. Try entering " + len(header_row_list) + " columns instead of " + len(row) + " columns.")

def add_person(csv_file):
    reader.file_read(csv_file)
    header_row = reader.header_row(csv_file)

    while True:
        
        newrow = input("Enter a row to add to the csv file\n").split(",")
        if len(header_row) == len(newrow):
            with open(csv_file, "a", newline="") as adder:
                exwrite = csv.writer(adder)

                exwrite.writerow(newrow)
                adder.close
                break
        else:
            print("Invalid format, Try again")

def csv_row_editer(csv_file):
    csv_list = []
    with open(csv_file, "r") as file:
        read_file = csv.reader(file)
        for row in read_file:
            csv_list.append(row)
    #print(csv_list)
    for i in range(len(csv_list)):
        print("Row " +  str(i) + ": " + str(csv_list[i]))
    edit_row = int(input("\nWhich row would you like to change? Enter 1 - " + str(len(csv_list)-1) + ":\n"))
    print( "Please enter the new details for each of the following :")
    for i in range(len(csv_list[0])):
        newRow = input("Enter new data for " + str(csv_list[0][i]) + " :")
        csv_list[edit_row][i] = newRow
    print("Row " + str(i) + " :" + str(csv_list[i]))

    change_csv = input("Do you want to save the changes? Enter (y) or (n)\n").lower()
    print(change_csv)
    if change_csv == "y":
        with open(csv_file, "w+") as file:
            read_file = csv.writer(file)
            for i in range(len(csv_list)):
                read_file.writerow(csv_list[i])

def csv_column_editer(csv_file):
    csv_list = []
    with open(csv_file, "r") as file:
        read_file = csv.reader(file)
        for row in read_file:
            csv_list.append(row)
    #print(csv_list)
    for i in range(len(csv_list)):
        print("Row " +  str(i) + ": " + str(csv_list[i]))
    edit_row = int(input("\nWhich row would you like to change? Enter 1 - " + str(len(csv_list)-1) + ":\n"))
    edit_column = int(input("\nWhich column do you want to edit? :\n"))
    print( "Please enter the new details for the selected column :")
    newRow = input("Enter new data for " + str(csv_list[0][edit_column]) + " :")
    csv_list[edit_row][edit_column] = newRow
    print("Row " + str(i) + " :" + str(csv_list[i]))

    change_csv = input("Do you want to save the changes? Enter (y) or (n)\n").lower()
    if change_csv == "y":
        with open(csv_file, "w+") as file:
            read_file = csv.writer(file)
            for i in range(len(csv_list)):
                read_file.writerow(csv_list[i])