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

    def review_text(self, text: str):
        review_prompt = f"""
        As an AI content reviewer, your task is to evaluate the following lines of code and extract database,
        schema, table, column, and aliases from each line of code. The extraction should be usable for quick
        documentation to allow for ease of understanding.

        Text:
        {text}

        Please extract the compenents with the following in mind:
        1. A namespace is the combination of database and schema listed as database.schema
        2. A column can be written as database.schema.table.column AS alias
        3. Column names can also be written as table.column or simply column, so you can work from right to left
        4. The alias usually follows an AS, but always follows the column name

        Your response should be returned in the following format:
        Database, Schema, Table, Column, Alias (this will be the header and each subsequent row should return entries from the Text)
        database_name, schema_name, table_name, column_name, alias_name
        """

        response = openai.ChatCompletion.create(
            engine = self.deployment_name,
            message = [
                {"role": "system", "content": "You are an expert code reviewer for documenting SQL logic and dependencies. Your task is to ensure all compenents of the logic are documented correctly"},
                {"role": "user", "content": review_prompt}
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