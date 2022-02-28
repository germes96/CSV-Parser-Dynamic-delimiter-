import argparse
#importing pandas as pd
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="EXCEL CSV Conviter with specific delimiter")
    parser.add_argument("-i", type=str, default="catalog.xlsx", help="Input file excel format")
    parser.add_argument("-o", type=str, default="result.csv", help="output file")
    parser.add_argument("-d", type=str, default="|", help="number of training epoch")
    args = parser.parse_args()
    print('PyCharm')
    read_file = pd.read_excel(args.i)
    read_file.to_csv(args.o,
                     index=None,
                     sep=args.d,
                     header=True)
