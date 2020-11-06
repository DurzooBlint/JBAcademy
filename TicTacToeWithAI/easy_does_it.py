import random


class Board:
    def __init__(self, s_input):
        self.s_input = s_input
        self.s_on_board = ""
        self.l_board = self.initiate_board()
        self.s_next = self.what_is_next()

    def clear_board(self):
        for row in self.l_board:
            for el in row:
                el = ' '
        self.s_input = ''
        self.s_on_board = ''

    def initiate_board(self):
        l_matrix = []
        l_row_a = [" ", " ", " "]
        l_row_b = [" ", " ", " "]
        l_row_c = [" ", " ", " "]

        l_matrix.append(l_row_a)
        l_matrix.append(l_row_b)
        l_matrix.append(l_row_c)

        return l_matrix

    def print_board(self):
        s_vertical = 9 * '-'
        i = 0
        s_row_a, s_row_b, s_row_c = '', '', ''

        for j in range(0, 3):
            s_row_a += (self.l_board[0][j])
            s_row_b += (self.l_board[1][j])
            s_row_c += (self.l_board[2][j])

        print(s_vertical)
        print('| ' + s_row_a.replace("", " ")[1: -1] + ' |')
        print('| ' + s_row_b.replace("", " ")[1: -1] + ' |')
        print('| ' + s_row_c.replace("", " ")[1: -1] + ' |')
        print(s_vertical)

    def what_is_next(self):
        i_x = self.s_on_board.count("X")
        i_o = self.s_on_board.count("O")

        if i_x <= i_o:
            return "X"
        else:
            return "O"

    def get_cell(self, i_row, i_column):
        i_row_t, i_column_t = transform_cords(i_row, i_column)
        s_result = self.l_board[i_row_t][i_column_t]
        return s_result

    def insert_cell(self, s_cords):
        if s_cords[-1] != 'c':
            l_cords = s_cords.split(" ")
            i_row_t, i_column_t = transform_cords(int(l_cords[0]), int(l_cords[1]))
        else:
            l_cords = s_cords[0:3].split(" ")
            i_row_t = int(l_cords[0])
            i_column_t = int(l_cords[1])

        s_value = self.what_is_next()
        self.l_board[i_row_t][i_column_t] = s_value
        self.s_on_board += s_value

    def get_score(self):
        l_main_diagonal = [[self.l_board[0][0], self.l_board[1][1], self.l_board[2][2]]]
        l_side_diagonal = [[self.l_board[0][2], self.l_board[1][1], self.l_board[2][0]]]
        l_vertical_0 = [[self.l_board[0][0], self.l_board[1][0], self.l_board[2][0]]]
        l_vertical_1 = [[self.l_board[0][1], self.l_board[1][1], self.l_board[1][2]]]
        l_vertical_2 = [[self.l_board[0][2], self.l_board[1][2], self.l_board[2][2]]]

        l_temp = l_main_diagonal + l_side_diagonal + self.l_board + l_vertical_0 + l_vertical_1 + l_vertical_2
        for row in l_temp:
            if row.count("X") == 3:
                s_result = "X wins"
                break
            elif row.count("O") == 3:
                s_result = "O wins"
                break
            elif len(self.s_on_board) == 9:
                s_result = "Draw"
                break
            else:
                s_result = ""
        return s_result


def validate_value(o_board, s_cords):
    s_result = ""

    if s_cords != "":
        l_cords = s_cords.split(" ")

        if l_cords[0].isnumeric() and l_cords[1].isnumeric():
            if 1 <= int(l_cords[0]) <= 3 and 1 <= int(l_cords[1]) <= 3:
                if o_board.get_cell(int(l_cords[0]), int(l_cords[1])) == " ":
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


def transform_cords(i_row, i_column):
    if i_row == 1 and i_column == 3:
        i_row_t = 0
        i_column_t = 0
    elif i_row == 2 and i_column == 3:
        i_row_t = 0
        i_column_t = 1
    elif i_row == 3 and i_column == 3:
        i_row_t = 0
        i_column_t = 2
    elif i_row == 1 and i_column == 2:
        i_row_t = 1
        i_column_t = 0
    elif i_row == 2 and i_column == 2:
        i_row_t = 1
        i_column_t = 1
    elif i_row == 3 and i_column == 2:
        i_row_t = 1
        i_column_t = 2
    elif i_row == 1 and i_column == 1:
        i_row_t = 2
        i_column_t = 0
    elif i_row == 2 and i_column == 1:
        i_row_t = 2
        i_column_t = 1
    elif i_row == 3 and i_column == 1:
        i_row_t = 2
        i_column_t = 2

    return i_row_t, i_column_t


def computer_moves(board):
    l_empty = []
    print('Making move level "easy"')
    i = 0
    for i in range(0, 3):
        j = 0
        for j in range(0, 3):
            if board.l_board[i][j] == " ":
                l_empty.append([i, j])
            j += 1
        i += 1

    i_random = random.randint(0, len(l_empty) - 1)
    s_cords = str(l_empty[i_random][0]) + " " + str(l_empty[i_random][1]) + 'c'
    board.insert_cell(s_cords)


def main():
    board = Board("")
    board.print_board()
    s_score = board.get_score()

    while s_score == "":
        if board.what_is_next() == "X":
            s_cords = input("Enter the coordinates: ")
            b_valid_value, s_error = validate_value(board, s_cords)
            if not b_valid_value:
                print(s_error)
            else:
                board.insert_cell(s_cords)
                board.print_board()
                s_score = board.get_score()
                if s_score != "":
                    print(s_score)
        else:
            computer_moves(board)
            board.print_board()
            s_score = board.get_score()
            if s_score != "":
                print(s_score)


if __name__ == "__main__":
    main()
