import re

def _col_formatter(col): 
    col = col.text.replace('\n', '').replace('  ', ' ').replace('  ', ' ')
    
    # remove thousands separators and make "." the decimal separator
    pattern = re.compile('[ ]*[-]*\d{1,3}(.\d{3})*(\,\d+)?')
    if pattern.match(col):
        col = col.replace('.', '')
        col = col.replace(',', '.')

    col = f'"{col}"'
    return col

def table_to_csv(table, file_name='table.csv'):
    rows = table.find_elements_by_tag_name("tr")
    with open(file_name, "w") as f:
        for row in rows:
            cols = row.find_elements_by_tag_name("td")
            formatted_cols = []
            for i in range(len(cols)):
                col = cols[i]
                if i > 0:
                    formatted_cols.append(_col_formatter(col))
                else:
                    formatted_cols.append(col.text.replace(' ', ''))

            f.write(",".join(formatted_cols) + "\n")
    return True