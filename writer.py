import csv

def file_write(header_row):
    with open(input("Enter the name of the file you want to create and set it to .csv\n"), "w") as csvfile:
        ex_write = csv.writer(csvfile)
        ex_write.writerow(header_row)

        while True:
            user_input = input("Enter row seperated by a comma (,)\nEnter (exit) to quit\n")
            if user_input == "exit":
                break
            row = user_input.split(",")
            if len(header_row) == len(row):
                ex_write.writerow(row)
            else:
                print("Invalid entry. Try entering " + len(header_row) + " columns instead of " + len(row) + " columns.")

def add_person(newrow):
    with open("testing1.csv", "a", newline="") as adder:
        exwrite = csv.writer(adder)
        exwrite.writerow(newrow)
        adder.close