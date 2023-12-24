matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
"""

matrix_rows = matrix_str.strip().split('\n')

max_row_length = max(len(row) for row in matrix_rows)

matrix_rows_padded = [row.ljust(max_row_length) for row in matrix_rows]

matrix_columns = [''.join(column) for column in zip(*matrix_rows_padded)]

secret_message = ''
for column in matrix_columns:
    alpha_chars = [char for char in column if char.isalpha()]
    secret_message += ''.join(alpha_chars) + ' '

secret_message = ' '.join(' '.join(group.split()) for group in secret_message.split())

print(secret_message)