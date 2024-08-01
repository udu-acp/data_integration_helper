# database_friendly_column_converter


### This snippet was created to expedite column normalization for use in Matillion DPC/ETL (or any other ETL tool with a create table component). I found myself having to remove spaces, hyphens, etc. as well as manually adding new lines when grabbing columns from any sort of CSV response/file. 

To use, add your own input and output column txt files, make sure the function arguments match your new names, add tab seperated columns into your input file (copy header from csv file to input text file), add any additional replace statements as needed, RUN, and grab your columns from the output file!
