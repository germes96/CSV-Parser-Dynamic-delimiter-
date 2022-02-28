# XLSX (EXCEL) to CSV Conviter
this module allows to convert excel and csv files by specifying the delimiter to use.

This is in order to take into account the content generally provided in excel files containing characters such as comma and semicolon. 

This python library will allow you to do this conversion by specifying more complex delimiters `('|', '$', '#')`. This will make it easier to process in your different server codes...etc. 

## Installation
```commandline
git clone <repository.git>
cd <repository>
pip install requiement.txt
```

## Basic usage
```commandline
python main.py
```
This basic usage considers the values for the execution parameters

- `Input File`: **catalog.xlsx** It is the file so the content must be parsed and written in a csv file
- `Output File`: **result.csv** Output file that contains the result of the processing
- `Delimiter`: This is the delimiter ("|" as default) that will be used to separate the content in `csv` file

## Advance usage
For more control, you can specify the value of each parameter. If a parameter is not specified then the default value specified above will be used.
```commandline
python main.py -i <InputFile> -o <OutputFile> -d <Delimiter>
```

### Examples

```commandline
python main.py -i iris.xlsx
```
The file `iris.xlsx` will be used as input document, the delimiter will be the character `'|'` and the result will be stored in `result.csv`.
```commandline
python main.py -i iris.xlsx -d '$'
```
The file `iris.xlsx` will be used as input document. The character `$` will be used to separate the elements in the file.
```commandline
python main.py -i iris.xlsx -o iris.csv -d '$'
```
Unlike the previous example, the output file is precise and is therefore `iris.csv`.
