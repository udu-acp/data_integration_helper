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

    
normalize_columns("input_columns.txt", "columns_normalized.txt")