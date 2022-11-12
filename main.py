from random import randint

SIZE = 10


class App:
    def __init__(self):
        self.board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        self.fleet = [5, 4, 3, 3, 2]

    def place_ships(self):
        for ship_length in self.fleet:
            direction = "EW" if randint(0, 1) == 0 else "NS"
            # print(f"{ship_length} {direction}")

            if direction == "EW":
                self.find_east_west_space(ship_length)
            else:
                self.find_north_south_space(ship_length)

    def find_east_west_space(self, ship_length):
        row = randint(0, SIZE-1)
        start_col = randint(0, SIZE-ship_length)
        end_col = start_col + ship_length - 1

    def find_north_south_space(self, ship_length):
        col = randint(0, SIZE-1)
        start_row = randint(0, SIZE-ship_length)
        end_row = start_row + ship_length - 1

    def print_board(self):
        for i in range(SIZE):
            for j in range(SIZE):
                print(self.board[i][j], end="  ")
            print()


if __name__ == '__main__':
    app = App()
    app.place_ships()
    app.print_board()
