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


def add_person(csv_file):
    reader.file_read(csv_file)
    header_row = reader.header_row(csv_file)

    while True:
        newrow = input("Enter a row separated by a comma (,) to add to the csv file\n").split(",")
        if len(header_row) == len(newrow):
            with open(csv_file, "a", newline="") as adder:
                exwrite = csv.writer(adder)

                exwrite.writerow(newrow)
            break
        else:
            print("Invalid format, Try again")


def csv_row_editer(csv_file):
    csv_list = reader.get_file_contents(csv_file)
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
        with open(csv_file, "w+") as file:
            read_file = csv.writer(file)
            for i in range(len(csv_list)):
                read_file.writerow(csv_list[i])


def csv_column_editer(csv_file):
    csv_list = reader.get_file_contents(csv_file)
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
