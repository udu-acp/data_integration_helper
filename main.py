from extractors import alias_extractor, normalize_columns, table_extractor



# normalize_columns("input_columns.txt", "columns_normalized.txt")
alias_extractor("input_columns.txt", "extracted_aliases.txt")
table_extractor("input_columns.txt", "extracted_tables.txt")