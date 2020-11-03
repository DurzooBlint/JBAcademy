def read_matrix(s_input):
    l_matrix = []
    l_row_a = []
    l_row_b = []
    l_row_c = []

    s_input = s_input.replace("_", " ")
    l_temp = [char for char in s_input]

    i = 0
    while i < len(l_temp):
        if i < 3:
            l_row_c.append(l_temp[i])
        elif 2 < i < 6:
            l_row_b.append(l_temp[i])
        else:
            l_row_a.append(l_temp[i])
        i += 1
    l_matrix.append(l_row_a)
    l_matrix.append(l_row_b)
    l_matrix.append(l_row_c)

    return l_matrix


def print_matrix(l_matrix):
    s_vertical = 9*'-'
    i = 0
    s_row_a, s_row_b, s_row_c = '', '', ''

    for j in range(0, 3):
        s_row_a += (l_matrix[0][j])
        s_row_b += (l_matrix[1][j])
        s_row_c += (l_matrix[2][j])

    # s_row_a = s_row_a.replace("_", " ")[0:]
    # s_row_b = s_row_b.replace("_", " ")[:]
    # s_row_c = s_row_c.replace("_", " ")[:]

    print(s_vertical)
    print('| ' + s_row_c.replace("", " ")[1: -1] + ' |')
    print('| ' + s_row_b.replace("", " ")[1: -1] + ' |')
    print('| ' + s_row_a.replace("", " ")[1: -1] + ' |')
    print(s_vertical)


def get_cell(i_row, i_column, l_matrix):
    s_result = l_matrix[i_row - 1][i_column - 1]
    return s_result


def validate_value(s_cords, l_matrix):
    s_result = ""
    l_cords = s_cords.split(" ")

    if l_cords[0].isnumeric() and l_cords[1].isnumeric():
        if 1 <= int(l_cords[0]) <= 3 and 1 <= int(l_cords[1]) <= 3:
            if get_cell(int(l_cords[0]), int(l_cords[1]), l_matrix) == " ":
                b_result = True
            else:
                b_result = False
                s_result = "This cell is occupied! Choose another one!"

        else:
            s_result = "Coordinates should be from 1 to 3!"
            b_result = False
    else:
        s_result = "You should enter numbers!"
        b_result = False

    return b_result, s_result


def insert_cell(l_matrix, s_cords, s_value):
    l_cords = s_cords.split(" ")
    # i_index = l_matrix[int(l_cords[0]) - 1].insert(int(l_cords[1]) - 1, s_value)
    l_matrix[int(l_cords[0]) - 1][int(l_cords[1]) - 1] = s_value
    return l_matrix

def main():
    s_input = input()
    l_matrix = read_matrix(s_input)
    print_matrix(l_matrix)

    s_cords = input("Enter the coordinates: ")
    b_valid_value, s_error = validate_value(s_cords, l_matrix)
    if not b_valid_value:
        print(s_error)
    else:
        s_value = 'X'
        insert_cell(l_matrix, s_cords, s_value)
    print_matrix(l_matrix)

if __name__ == "__main__":
    main()
