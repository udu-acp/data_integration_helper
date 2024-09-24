from extractors import alias_extractor, column_counter, normalize_columns, table_extractor
from generator import ExtractionGenerator



# normalize_columns("input_columns.txt", "columns_normalized.txt")
# alias_extractor("input_columns.txt", "extracted_aliases.txt")
# table_extractor("input_columns.txt", "extracted_tables.txt")
# column_counter("input_columns.txt", "extracted_counts.txt")

# if input("Review or Document?") == "Review":
#     extract_generator = ExtractionGenerator()

#     input_path = "input_columns.txt"

#     with open(input_path, 'rb') as f:
#         input_content = f.read()

#     data_documentation = extract_generator.review_text(input_content) 

#     output_path = "extracted_ai_document.txt"
#     with open(output_path, 'w') as f:
#         f.write(data_documentation)


extract_generator = ExtractionGenerator()

# data_documentation = extract_generator.review_columns("input_columns.txt")
data_documentation = extract_generator.sql_extractor("input_columns.txt")
print(data_documentation)
