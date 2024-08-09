# data_integration_helper

### This repo is a work-in-progress. As I find myself performing redundant/arduous tasks, I'll develop functions to expedite the process. The goal is to perpetually optimize for efficiency.

#### normalize_columns:
The normalize_columns function was created to simplify column normalization for use in Matillion DPC/ETL or any other ETL tool with a table creation component. It helps remove spaces, hyphens, and other unwanted characters, and it automates the addition of new lines when processing columns from CSV files.

Usage Instructions: 
1. Add your input and output column text files.
2. Ensure that the function arguments correspond to your new file names.
3. Insert tab-separated columns into your input file (you can copy the header from your CSV file to the input text file).
4. Add any additional replace statements as needed.
5. Run the function and retrieve your columns from the output file.
