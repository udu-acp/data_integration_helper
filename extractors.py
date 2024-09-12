import numpy as np

def normalize_columns(input_file, output_file):
    # access the txt file with columns listed
    columns_file = open(input_file, 'r')

    # read the file into variable
    data = columns_file.read()

    ### add any additional characters that need to replaced here
    # replace any tabs with newlines
    # replace % with pct
    # replace - with _
    data = data.replace('\t', '\n').replace('%', 'pct').replace('-', '_')

    # then split the text by newlines 
    data_into_list = data.split('\n')

    # create list to hold updated columns
    data_without_spaces = []

    # remove trailing ' ' in list elements then
    # replace remaining ' ' and '/' with '_'
    for column in data_into_list:
        data_without_spaces.append(column.strip().replace(' ', '_').replace('/', '_'))

    # read columns to new file
    with open(output_file, 'w+') as f:

        for column in data_without_spaces:
            # print each column in uppercase
            print(column.upper(), file=f)


def alias_extractor(input_file, output_file):
    # access the txt file with columns listed
    columns_file = open(input_file, 'r+')

    # read the file into variable
    data = columns_file.read()

    # remove quotes, commas, and split by newline
    columns_list = data.replace('"','').replace(',', '').split('\n')

    # create empy list to store updated aliases
    aliases = []

    for column in columns_list:
        # split each item and capitalize
        alias_parts = column.upper().split(" AS ")

        # check if the split portion is a certain size
        if len(alias_parts) > 1:
            # append the second part of the split line
            result = alias_parts[1]
            aliases.append(result)
    
    # print the list into output file in titlecase
    with open(output_file, 'w+') as f:
        for column in aliases:
            print(column.title(), file=f)


def table_extractor(input_file, output_file):
    # access the txt file with columns listed
    columns_file = open(input_file, 'r+')

    # read the file into variable
    data = columns_file.read()

    # remove quotes, commas, and split by newline
    columns_list = data.replace('"','').replace(',', '').split('\n')

    # create empy list to store updated aliases
    tables = []

    for column in columns_list:
        # store the first substring from the split column
        table_parts = column.split('.')[0]
        
        # append to tables
        tables.append(table_parts)

    # print the list into output file in titlecase
    with open(output_file, 'w+') as f:
        for column in tables:
            print(column.title(), file=f)


def counts(list, string):
    # loop through elements in a list and count their occurances
    count = 0
    for element in list:
        if element == string:
            count += 1
    return count

def column_counter(input_file, output_file):
    # read file and enforce uniformity into a list
    data = open(input_file, 'r+')
    data = data.read()
    columns_cleaned = data.replace('"', '').replace(',', '').strip()
    columns_list = columns_cleaned.lower().replace(' ', '_').split('\n')

    # write out the columns and their use counts
    with open(output_file, 'w+') as f:
        for column in columns_list:
            column = column.split(".")[-1]
            print(f"{column}, {counts(columns_list, column)}", file=f)

    # remove duplicate column names and counts. then store in list
    counts_data = open(output_file, 'r+')
    counts_data = counts_data.read()
    counts_list = counts_data.strip().split('\n')
    unique_list = np.unique(counts_list)

    # loop through list and print
    with open(output_file, 'w+') as f:
        print("column_name, count", file=f)
        for record in unique_list:
            print(record, file=f)

