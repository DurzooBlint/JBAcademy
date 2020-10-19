def read_matrix(i_number_rows, l_matrix_a):
    l_matrix = []

    lines = l_matrix_a.split('\n')

    i = 0
    while i < i_number_rows:
        l_matrix.append(list(map(float, lines[i].split(' '))))
        i += 1

    return l_matrix


def print_matrix(l_matrix):
    for row in l_matrix:
        str_ = ''
        for num in row:
            str_ += ' ' + str(num)
        print(str_.strip())


def add_matrices(l_matrix_a, l_matrix_b):
    l_matrix = []

    i_rows_a = len(l_matrix_a)
    i_columns_a = len(l_matrix_a[0])
    i_rows_b = len(l_matrix_b)
    i_columns_b = len(l_matrix_b[0])

    if i_rows_a != i_rows_b or i_columns_a != i_columns_b:
        print("ERROR")
    else:

        for i in range(i_rows_a):
            l_row_a = l_matrix_a[i]
            l_row_b = l_matrix_b[i]
            l_row_result = list(map(lambda x, y: x + y, l_row_a, l_row_b))
            l_matrix.append(l_row_result)

    return l_matrix


def multiply_matrix_constant(l_matrix_a, i_constant):
    l_matrix = []

    for i in l_matrix_a:
        l_row_result = []
        for item in i:
            l_row_result.append(float(item) * i_constant)
        l_matrix.append(l_row_result)

    return l_matrix


def get_row(l_matrix, i_row):
    return l_matrix[i_row - 1]


def get_column(l_matrix, i_column):
    l_result = []
    for row in l_matrix:
        l_result.append(row[i_column - 1])
    return l_result


def dot_product(l_row, l_column):
    i_result = 0
    i = 0
    while i < len(l_row):
        i_result += l_row[i] * l_column[i]
        i += 1
    return i_result


def multiply_matrices(l_matrix_a, i_rows_a, i_columns_a, l_matrix_b, i_rows_b, i_columns_b):
    l_matrix = []

    i_rows_c = i_rows_a
    i_columns_c = i_columns_b

    if i_columns_a == i_rows_b:
        # create C matrix
        l_matrix = []
        row = 1
        column = 1
        while row <= i_rows_c:
            l_rows_c = []
            column = 1
            while column <= i_columns_c:
                l_row_a = get_row(l_matrix_a, row)
                l_column_b = get_column(l_matrix_b, column)
                l_rows_c.append(dot_product(l_row_a, l_column_b))
                column += 1
            l_matrix.append(l_rows_c)
            row += 1
    else:
        print('The operation cannot be performed.')
    return l_matrix


def print_menu():
    print('')
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('0. Exit')


def main():

    print_menu()
    option = int(input())
    while option != 0:
        if option == 1:  # Add matrices
            # read size of 1st matrix, take number of rows
            temp = input('Enter size of first matrix: ')
            i_size_a = int(temp.split(' ')[0])

            # read 1st matrix
            temp = input('Enter first matrix: ')
            s_input_a = temp + '\n'
            for item in range(i_size_a - 1):
                temp = input()
                if item < (i_size_a - 2):
                    s_input_a += temp + '\n'
                else:
                    s_input_a += temp
            l_matrix_a = read_matrix(i_size_a, s_input_a)

            # read size of 2nd matrix, take number of rows
            temp = input('Enter size of second matrix: ')
            i_size_b = int(temp.split(' ')[0])
            # read 2nd matrix
            temp = input('Enter second matrix: ')
            s_input_b = temp + '\n'
            for item in range(i_size_b - 1):
                temp = input()
                if item < i_size_b - 2:
                    s_input_b += temp + '\n'
                else:
                    s_input_b += temp
            l_matrix_b = read_matrix(i_size_b, s_input_b)
            l_result = add_matrices(l_matrix_a, l_matrix_b)
            print('The result is: ')
            print_matrix(l_result)

        elif option == 2:  # Multiply matrix by constant
            # read size of matrix, take number of rows
            temp = input('Enter size of matrix: ')
            i_size = int(temp.split(' ')[0])

            # read matrix
            temp = input('Enter matrix: ')
            s_input_a = temp + '\n'
            for item in range(i_size - 1):
                temp = input()
                if item < (i_size - 2):
                    s_input_a += temp + '\n'
                else:
                    s_input_a += temp
            l_matrix = read_matrix(i_size, s_input_a)

            # read constant
            constant = int(input('Enter constant: '))
            l_result = multiply_matrix_constant(l_matrix, constant)
            print('The result is: ')
            print_matrix(l_result)

        elif option == 3:  # Multiply matrix by matrix
            # read size of 1st matrix, take number of rows
            temp = input('Enter size of first matrix: ')
            i_rows_a = int(temp.split(' ')[0])
            i_columns_a = int(temp.split(' ')[1])

            # read 1st matrix
            temp = input('Enter first matrix: ')
            s_input_a = temp + '\n'
            for item in range(i_rows_a - 1):
                temp = input()
                if item < (i_rows_a - 2):
                    s_input_a += temp + '\n'
                else:
                    s_input_a += temp
            l_matrix_a = read_matrix(i_rows_a, s_input_a)

            # read size of 2nd matrix, take number of rows
            temp = input('Enter size of second matrix: ')
            i_rows_b = int(temp.split(' ')[0])
            i_columns_b = int(temp.split(' ')[1])
            # read 2nd matrix
            temp = input('Enter second matrix: ')
            s_input_b = temp + '\n'
            for item in range(i_rows_b - 1):
                temp = input()
                if item < i_rows_b - 2:
                    s_input_b += temp + '\n'
                else:
                    s_input_b += temp
            l_matrix_b = read_matrix(i_rows_b, s_input_b)
            l_result = multiply_matrices(l_matrix_a, i_rows_a, i_columns_a, l_matrix_b, i_rows_b, i_columns_b)
            print('The result is: ')
            print_matrix(l_result)

        print_menu()
        option = int(input())


if __name__ == "__main__":
    main()