from extractors import alias_extractor, column_counter, normalize_columns, table_extractor
from generator import ExtractionGenerator



# normalize_columns("input_columns.txt", "columns_normalized.txt")
# alias_extractor("input_columns.txt", "extracted_aliases.txt")
# table_extractor("input_columns.txt", "extracted_tables.txt")
# column_counter("input_columns.txt", "extracted_counts.txt")



extract_generator = ExtractionGenerator()
data_documentation = extract_generator.sql_extractor("input_columns.txt")
print(data_documentation)
