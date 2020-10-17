def read_matrix(s_input):
    l_matrix = []
    lines = s_input.split('\n')
    i_rows_a = int(lines[0].split(' ')[0])

    i = 1
    while i <= i_rows_a:
        l_matrix.append(list(map(int, lines[i].split(' '))))
        i += 1
    return l_matrix


def read_matrices(s_input):
    l_matrix_a = []
    l_matrix_b = []
    lines = s_input.split('\n')
    i_rows_a = int(lines[0].split(' ')[0])

    i = 1
    while i <= i_rows_a:
        l_matrix_a.append(list(map(int, lines[i].split(' '))))
        i += 1

    i_rows_b = int(lines[i_rows_a + 1].split(' ')[0])

    r = i_rows_b + 2
    while r <= i_rows_a + i_rows_b + 1:
        l_matrix_b.append(list(map(int, lines[r].split(' '))))
        r += 1

    return l_matrix_a, l_matrix_b


def matrix_addition(l_a, l_b):
    l_result = list()
    i_rows_a = len(l_a)
    i_columns_a = len(l_a[0])
    i_rows_b = len(l_b)
    i_columns_b = len(l_b[0])

    if i_rows_a != i_rows_b or i_columns_a != i_columns_b:
        print("ERROR")
    else:

        for i in range(i_rows_a):
            l_row_a = l_a[i]
            l_row_b = l_b[i]
            l_row_result = list(map(lambda x, y: x + y, l_row_a, l_row_b))
            l_result.append(l_row_result)

    return l_result


def matrix_multiplication_constant(l_a, constant):
    l_result = list()
    l_result = list()
    #i_rows_a = len(l_a)

    for i in l_a:
        l_row_result =[]
        for item in i:
            l_row_result.append(int(item) * constant)
        l_result.append(l_row_result)

    return l_result


def main():
    temp = input()
    s_input = temp + '\n'
    i_rows_a = int(temp[0].split(' ')[0])

    for l in range(i_rows_a):
        temp = input()
        if l < i_rows_a-1:
            s_input += temp + '\n'
        else:
            s_input += temp

    constant = int(input())
    # s_input += temp
    # i_rows_a = int(temp[0].split(' ')[0])
    l_matrix_a = read_matrix(s_input)
    l_result = matrix_multiplication_constant(l_matrix_a, constant)

    for row in l_result:
        str_ = ''
        for num in row:
            str_ += ' ' + str(num)
        print(str_.strip())


if __name__ == "__main__":
    main()
