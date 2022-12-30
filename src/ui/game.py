
from ui.quit import Quit
from ui.seed import SeedUI
from game.board import Board
from game.board_utils import Utils as utils
from game.board_utils import BoardState, Direction
from ui.menu import Menu
import numpy as np


class GameUI():
    def __init__(self):
        self.seed_ui = SeedUI()
        self.menu = Menu()

    def view(self):
        seed = self.seed_ui.view()
        board = Board(seed)
        print(utils.board_to_string(board))

        commands = [
            {
                "action": Direction.UP,
                "message": "↑",
                "shortcut": "w"
            },
            {
                "action": Direction.DOWN,
                "message": "↓",
                "shortcut": "s"
            },
            {
                "action": Direction.LEFT,
                "message": "←",
                "shortcut": "a"
            },
            {
                "action": Direction.RIGHT,
                "message": "→",
                "shortcut": "d"
            },
            {
                "action": self.__quit_game,
                "message": "Quit game",
                "shortcut": "q"
            }
        ]

        while True:
            try:
                command = self.menu.show(commands, cancel=False)
                if callable(command):
                    command()
                else:
                    board.move(command)
                    print(utils.board_to_string(board, redraw=True))
                    if board.state == BoardState.LOST:
                        print("GAME LOST!")
                        self.__quit_game()
                    elif board.state == BoardState.WON:
                        print("GAME WON!")
                        self.__quit_game()
            except Quit:
                break

    def __quit_game(self):
        raise Quit
