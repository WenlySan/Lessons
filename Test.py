import tkinter as tk


class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Шахматная доска")
        self._build_chess_board()

    def _build_chess_board(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                frame = tk.Frame(self, width=50, height=50, bg=color)
                frame.grid(row=row, column=col)


if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.mainloop()

