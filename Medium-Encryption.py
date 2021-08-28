def encryption(s):
    chars_without_spaces = [i for i in s if i != " "]
    rows_number = int((len(chars_without_spaces)**0.5)//1)
    if rows_number**2 >= len(chars_without_spaces):
        columns_number = rows_number
    elif rows_number*(rows_number+1) >= len(chars_without_spaces):
        columns_number = rows_number + 1
    else:
        columns_number = rows_number + 1
        rows_number += 1
    rows = []
    for k in range(rows_number):
        row = ""
        for i in range(columns_number*k,columns_number*k+columns_number):
            try:
                row += chars_without_spaces[i]
            except IndexError:
                pass
        rows.append(row)
    final_string = ""
    for i in range(columns_number):
        string = ""
        for k in range(rows_number):
            try:
                string += rows[k][i]
            except IndexError:
                continue
        final_string += (string + " ")
    return final_string
