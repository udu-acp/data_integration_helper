def normalize_columns(file_path, output_file):
    # access the txt file with columns listed
    columns_file = open(file_path, 'r')

    # read the file into variable
    data = columns_file.read()

    # replace any tabs with '' and split the text by newlines 
    data_into_list = data.replace('\t', '').split('\n')

    # create list to hold updated columns
    data_without_spaces = []

    # remove trailing ' ' in list elements then
    # replace remaining ' ' and '/' with '_'
    for column in data_into_list:
        data_without_spaces.append(column.strip().replace(' ', '_').replace('/', '_'))

    # read columns to new file
    with open(output_file, 'w+') as f:

        for column in data_without_spaces:
            print(column, file=f)

    
normalize_columns("columns.txt", "columns_normalized.txt")