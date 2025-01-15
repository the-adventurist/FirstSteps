def print_table(info):
    col_widths = [0] * len(info)
    for c in range(len(info)):
        for cell in range(len(info[0])):
            col_widths[c] = max(len(info[c][0]), len(info[c][1]), len(info[c][2]), len(info[c][3]))

    for c in range(len(info)):
        for cell in range(len(info[0]) - 1):
            print(info[cell][c].rjust(col_widths[cell]), end=' ')
            if cell == 2 and c == 2:
                print()
                print(info[0][c + 1].rjust(col_widths[0]), info[1][c + 1].rjust(col_widths[1]),
                      info[2][c + 1].rjust(col_widths[2]))
        print()



table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)