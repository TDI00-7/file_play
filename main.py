import argparse
import writer
import reader

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--header-row", nargs="+", default= [])
    args = parser.parse_args()
    #writer.file_write(args.header_row)
    reader.file_read(input("Enter Name of csv file you wish to open\n"))
    writer.add_person(args.header_row)



if __name__ == "__main__":
    main()