class Board:
    def __init__(self, s_input):
        self.s_input = s_input
        self.s_on_board = self.s_input[:].replace("_", "")
        self.l_board = self.initiate_board()
        self.s_next = self.what_is_next()

    def initiate_board(self):
        l_matrix = []
        l_row_a = []
        l_row_b = []
        l_row_c = []

        self.s_input = self.s_input.replace("_", " ")
        l_temp = [char for char in self.s_input]

        i = 0
        while i < len(l_temp):
            if i < 3:
                l_row_a.append(l_temp[i])
            elif 2 < i < 6:
                l_row_b.append(l_temp[i])
            else:
                l_row_c.append(l_temp[i])
            i += 1
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
        l_cords = s_cords.split(" ")
        i_row_t, i_column_t = transform_cords(int(l_cords[0]), int(l_cords[1]))
        s_value = self.what_is_next()
        self.l_board[i_row_t][i_column_t] = s_value
        self.s_on_board += s_value

    def get_score(self):
        l_main_diagonal = [[self.l_board[0][0], self.l_board[1][1], self.l_board[2][2]]]
        l_side_diagonal = [[self.l_board[0][2], self.l_board[1][1], self.l_board[2][0]]]
        l_temp = l_main_diagonal + l_side_diagonal + self.l_board
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
    # else:
    #     if len(o_board.s_on_board) == 9:
    #         s_result = "Draw"
    #     else:
    #         s_result = "Game not finished"
    #     b_result = False

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
    # else:
    #     if len(o_board.s_on_board) == 9:
    #         s_result = "Draw"
    #     else:
    #         s_result = "Game not finished"
    #     b_result = False

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


def main():
    s_input = input()
    board = Board(s_input)
    # _XXOO_OX_
    s_score = board.get_score()
    board.print_board()

    while s_score == "" and len(board.s_on_board) == len(board.s_input.replace(" ", "")):
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
            elif len(board.s_on_board) == len(board.s_input.replace(" ", "")) + 1:
                print("Game not finished")


if __name__ == "__main__":
    main()
