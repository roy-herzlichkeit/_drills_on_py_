import sys

Digits = [["  0000  ", " 0    0 ", "0       0", "0       0", "0       0", "0       0",  " 0    0 ", "  0000  "], ["      11", "     1 1", "    1  1", "   1   1", "       1", "       1", "       1", "11111111"],["22222222", "   2     2", "   2    2 ", "      2  ", "     2   ", "    2    ", "   2     ", "   22222"], ["33333333", "       3", "       3", "    3333",  "       3", "       3", "       3", "33333333"], ["      44", "     4 4", "    4  4", "   4   4", "   44444", "       4", "       4", "       4"], ["55555555", "5        ", "5        ", "5555555  ", "       5 ", "       5 ", "5      5 ", " 555555  "], ["  6666  ", " 6      ", "6       ", "6666666 ", "6      6", "6      6", " 6    6 ", "  6666  "], ["77777777", "      7 ", "     7  ", "    7   ", "   7    ", "  7     ", " 7      ", "7       "], ["  8888  ", " 8    8 ", "8      8", "  8888  ", "8      8", "8      8", " 8    8 ", "  8888  "], ["  9999  ", " 9    9 ", "9      9", "9      9", "  99999 ", "       9", "      9 ", "  9999  "]]

def main():
    try:
        digits = sys.argv[1]
        row = 0
        while row < 8:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                line += digit[row] + "\t\t"
                column += 1
            print(line)
            row += 1
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", digits)

if __name__ == "__main__":
    main()