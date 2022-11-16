from random import randint

SIZE = 10


class App:
    def __init__(self):
        self.board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        self.fleet = [5, 4, 3, 3, 2]

    def place_ships(self):
        for ship_length in self.fleet:
            direction = "H" if randint(0, 1) == 0 else "V"
            # print(f"{ship_length} {direction}")

            if direction == "EW":
                self.find_horizontal_space(ship_length)
            else:
                self.find_vertical_space(ship_length)

    def find_horizontal_space(self, ship_length: int):
        row = randint(0, SIZE-1)
        start_col = randint(0, SIZE-ship_length)
        end_col = start_col + ship_length - 1

    def find_vertical_space(self, ship_length: int):
        col = randint(0, SIZE-1)
        start_row = randint(0, SIZE-ship_length)
        end_row = start_row + ship_length - 1

    def ship_will_fit_in_row(self, row: int, start_col: int, ship_length: int) -> bool:
        for col in range(start_col, start_col+ship_length):
            if self.board[row][col] != 0:
                return False
        return True

    def ship_will_fit_in_col(self, col: int, start_row: int, ship_length: int) -> bool:
        for row in range(start_row, start_row+ship_length):
            if self.board[row][col] != 0:
                return False
        return True

    def print_board(self):
        for i in range(SIZE):
            for j in range(SIZE):
                print(self.board[i][j], end="  ")
            print()


if __name__ == '__main__':
    app = App()
    app.place_ships()
    app.print_board()
