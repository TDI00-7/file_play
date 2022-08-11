import argparse
import writer
import reader

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--header-row", nargs="+", default= [])
    args = parser.parse_args()
    
    while True:
        user_choice = input("\nWhat you want:\n(1)Create CSV\n(2)Read CSV\n(3)Add Row to CSV\n(4)Modify row in CSV\n(5)Edit Cell in csv file\n(6)Exit\n")
        if user_choice == "1":
            writer.file_write(input("Enter name for csv file : "))
        elif user_choice == "2":
            reader.file_read(input("Enter Name of csv file you wish to open: "))
        elif user_choice == "3":
            writer.add_person(input("Enter Name of csv file you wish to add to: "))
        elif user_choice == "4":
            writer.csv_row_editer(input("Enter Name of csv file you wish to add to: "))
        elif user_choice == "5":
            writer.csv_column_editer(input("Enter Name of csv file you wish to add to: "))
        elif user_choice == "6":
            break
        else:
            print("Invalid option try again")

    
    



if __name__ == "__main__":
    main()