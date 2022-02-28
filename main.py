
#importing pandas as pd
import pandas as pd
import csv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    read_file = pd.read_excel("catalog.xlsx")
    read_file.to_csv("catalog.csv",
                     index=None,
                     sep="|",
                     header=True)
