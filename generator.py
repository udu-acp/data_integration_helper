import os
from dotenv import load_dotenv
import openai

class ExtractionGenerator:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("AZURE_OPENAI_KEY")
        openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        openai.api_type = 'azure'
        openai.api_version = '2023-05-15'
        self.deployment_name = 'AI_AmplifyCP_GPT4o'

    def review_columns(self, input_file):
        with open(input_file, 'r') as f:
            input_content = f.read()

        review_prompt = f"""
        As an AI content reviewer, your task is to evaluate the following lines of code and extract database,
        schema, table, column, and aliases from each line of code. The extraction should be usable for quick
        documentation to allow for ease of understanding.

        Text:
        {input_content}

        Please extract the compenents with the following in mind:
        1. A namespace is the combination of database and schema listed as database.schema
        2. A column can be written as database.schema.table.column AS alias
        3. Column names can also be written as table.column or simply column, so you can work from right to left
        4. The alias usually follows an AS, but always follows the column name

        Your response should be returned in the following format:
        Database, Schema, Table, Column, Alias (this will be the header and each subsequent row should return entries from the Text)
        database_name, schema_name, table_name, column_name, alias_name


        After generating the response, review it to ensure:
        1. All provided information is in column form under database, schema, table, column, and alias
        2. If a column's result is empty, instead of N/A use NULL
        """

        response = openai.ChatCompletion.create(
            engine = self.deployment_name,
            messages = [
                {"role": "system", "content": "You are an expert code reviewer for documenting SQL logic and dependencies. Your task is to ensure all compenents of the logic are documented correctly"},
                {"role": "user", "content": f"{review_prompt}"}
            ],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.2,
        )

        if response.choices and response.choices[0].message:
            return response.choices[0].message.content.strip()
        else:
            return "Error: Unable to review content."
        
    def sql_extractor(self, input_file):
        with open(input_file, 'r') as f:
            input_content = f.read()

        review_prompt = f"""
        As an AI SQL code reviewer, your task is to evaluate the following lines of SQL code and docuemnt the dependencies for the logic.
        This includes extracting the database, schema, table/CTE, column, aliases, and logic for each column.
        Look through select statements, taking note of the database.schema.tables beign referenced and any associated alias to help
            document the dependencies of each column list.
        The extraction should be usable for quick documentation to allow for ease of understanding.

        Text:
        {input_content}

        Please extract the compenents with the following in mind:
        1. A namespace is the combination of database and schema listed as database.schema
        2. A column can be written as database.schema.table.column AS alias
        3. A column can also be logic like cast(timestamp as date) AS alias or datedif(table.column, table.column2) AS alias.
        4. A column can also be written as table.column or simply column, so you can work from right to left
        5. If the column is actually logic, record the logic (i.e. case(timestamp as date))
        6. The alias usually follows an AS, but always follows the column name
        7. Aliases can also be used for objects (FROM database.schema.table as alias)
        8. Table aliases can then be used in column definitions (table_alias.column)

        Your response should be returned in the following format:
        Database, Schema, Table, Column, Alias (this will be the header and each subsequent row should return entries from the Text)
        database_name, schema_name, table_name, column_name, alias_name


        After generating the response, review it to ensure:
        1. All provided information is in column form under database, schema, table/CTE, column, alias, and logic
        2. If a table alias was used, document the original table name instead.
        3. If the same table is referenced twice and given two different aliases, still use the same table name, but leave a note in the review section to discern which rows came from which alias
        4. If a column's result is empty, instead of N/A use NULL
        5. If a CTE is used, write full table name of the tables the CTE is derived from in the review notes
        6. The logic column should include the logic used to create the alias, if this doesn't apply use the database.schema.table.column name
        7. Mention where filters are applied (both the tables and logic)
        8. Return the columns in CSV format
        9. Break up the notes into different sections (General Notes, Logic, Table Aliases, CTEs Used, and Filters Applied)
        10. Always include review notes
        """

        response = openai.ChatCompletion.create(
            engine = self.deployment_name,
            messages = [
                {"role": "system", "content": "You are an expert code reviewer for documenting SQL logic and dependencies. Your task is to ensure all compenents of the logic are documented correctly"},
                {"role": "user", "content": f"{review_prompt}"}
            ],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.2,
        )

        if response.choices and response.choices[0].message:
            return response.choices[0].message.content.strip()
        else:
            return "Error: Unable to review content."