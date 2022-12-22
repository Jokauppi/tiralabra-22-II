import numpy as np
from enum import Enum


class Utils():
    def __init__(self):
        pass

    def empty_tiles(board):
        tiles = board.board
        empty_tiles = []
        with np.nditer(tiles, flags=['multi_index'], op_flags=['readwrite']) as it:
            for tile in it:
                if tile == 0:
                    empty_tiles.append(it.multi_index)
        return (empty_tiles)

    def move_line_forwards(line):

        p1 = len(line) - 2
        p2 = len(line) - 1

        modified = False

        while True:
            if p1 == -1:
                break
            elif line[p1] > 0 and line[p2] == 0:
                line[p2] = line[p1]
                line[p1] = 0
                p1 -= 1
                modified = True
            elif line[p1] == 0:
                p1 -= 1
            elif line[p1] == line[p2]:
                line[p2] = line[p1] + line[p2]
                line[p1] = 0
                p1 -= 1
                p2 -= 1
                modified = True
            elif line[p1] > 0 and line[p2] > 0:
                if p2 - 1 == p1:
                    p1 -= 1
                    p2 -= 1
                else:
                    p2 -= 1
            else:
                raise Exception("unnoticed line push case")

        return (line, modified)

    def move_line_backwards(line):

        max = len(line)
        p1 = 0
        p2 = 1

        modified = False

        while True:
            if p2 == max:
                break
            elif line[p2] > 0 and line[p1] == 0:
                line[p1] = line[p2]
                line[p2] = 0
                p2 += 1
                modified = True
            elif line[p2] == 0:
                p2 += 1
            elif line[p1] == line[p2]:
                line[p1] = line[p1] + line[p2]
                line[p2] = 0
                p1 += 1
                p2 += 1
                modified = True
            elif line[p1] > 0 and line[p2] > 0:
                if p1 + 1 == p2:
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1
            else:
                raise Exception("unnoticed line push case")

        return (line, modified)

    def print_board(board, size, redraw=False):

        if redraw:
            start_line = (2 * size + 1) * "\033[F" + "╔" + (size - 1) * "════╦" + "════╗\n"
        else:
            start_line = "╔" + (size - 1) * "════╦" + "════╗\n"

        middle_lines = ""
        separator = "╠" + (size - 1) * "════╬" + "════╣\n"

        for index in range(size):
            row = board[index]
            number_line = "║"
            for number in row:
                if number == 0:
                    number_line += '\33[30m{:4d}\33[0m║'.format(number)
                elif number > 64:
                    number_line += '\33[33m{:4d}\33[0m║'.format(number)
                elif number > 4:
                    number_line += '\33[31m{:4d}\33[0m║'.format(number)
                else:
                    number_line += '{:4d}║'.format(number)
            number_line += "\n"
            middle_lines += number_line
            if index < size - 1:
                middle_lines += separator

        end_line = "╚" + (size - 1) * "════╩" + "════╝"

        print(start_line + middle_lines + end_line)


class BoardState(Enum):
    INPROGRESS = 1
    LOST = 2
    WON = 3
