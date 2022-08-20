import csv
import reader


def file_write(filename):

    # We are calling split directly on the input because we only care about working with the
    # input as a list data type.
    header_row_list = input("Enter Header Row using (,) to seperate the columns\n").split(',')
    with open(input(filename), "w") as csvfile:
        ex_write = csv.writer(csvfile)
        ex_write.writerow(",".join(header_row_list))

        while True:
            # We are NOT calling split directly on the input here beacuse we need to check if
            # the user inputs the exact string 'exit', in which case we need to break out of
            # the loop.
            user_input = input("Enter row seperated by a comma (,)\nEnter (exit) to quit\n")
            if user_input == "exit":
                break

            row = user_input.split(",")
            if len(header_row_list) == len(row):
                ex_write.writerow(row)
            else:
                print(f"Invalid entry. Try entering {len(header_row_list)} columns instead of {len(row)} columns.")


def add_person(filename):
    reader.file_read(filename)
    header_row = reader.header_row(filename)

    #Used a while loop to allow multiple row to be added to the csv
    #at a time.
    while True:
        newrow = input(f"Enter a row separated by a comma (,) to add to the csv file. Type (exit) to stop.\n")
        if newrow == "exit":
            break
    #After i check to make sure the user doesnt want to exit
    #I have to split the string apart
        newrow = newrow.split(",")
        if len(header_row) == len(newrow):
            with open(filename, "a", newline="") as adder:
                exwrite = csv.writer(adder)
                exwrite.writerow(newrow)
        elif len(header_row) != len(newrow):
            print("Invalid format, Try again")


def csv_row_editer(filename):
    csv_list = reader.get_file_contents(filename)
    for i in range(len(csv_list)):
        print(f'Row {i}: {",".join(csv_list[i])}')

    edit_row = int(input(f"\nWhich row would you like to change? Enter 1 - {len(csv_list)-1}:\n"))
    print( "Please enter the new details for each of the following :")
    for i in range(len(csv_list[0])):
        newRow = input(f"Enter new data for {csv_list[0][i]}:")
        csv_list[edit_row][i] = newRow
    print(f"Row {i}: {csv_list[i]}")

    change_csv = input("Do you want to save the changes? Enter (y) or (n)\n").lower()
    print(change_csv)
    if change_csv == "y":
        with open(filename, "w+") as file:
            read_file = csv.writer(file)
            for i in range(len(csv_list)):
                read_file.writerow(csv_list[i])


def csv_column_editer(filename):
    csv_list = reader.get_file_contents(filename)
    #print(csv_list)
    for i in range(len(csv_list)):
        print(f"Row {i}: {csv_list[i]}")
    edit_row = int(input(f"\nWhich row would you like to change? Enter 1 - {len(csv_list)-1}: "))
    edit_column = int(input(f"\nWhich column do you want to edit? :\n"))
    print(f"Please enter the new details for the selected column :")
    newRow = input(f"Enter new data for {csv_list[0][edit_column]}:")
    csv_list[edit_row][edit_column] = newRow
    print(f"Row {i}: {csv_list[i]}")

    while True:
        change_csv = input(f"Do you want to save the changes? Enter (y) or (n)\n").lower()
        if change_csv == "y":
            with open(filename, "w+") as file:
                read_file = csv.writer(file)
                for i in range(len(csv_list)):
                    read_file.writerow(csv_list[i])
            break
        elif change_csv == "n":
            break
        else:
            print(f"invald option")
