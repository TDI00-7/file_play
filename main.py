import argparse
import writer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--header-row", nargs="+", default=[])
    args = parser.parse_args()
    writer.file_write(args.header_row)



if __name__ == "__main__":
    main()