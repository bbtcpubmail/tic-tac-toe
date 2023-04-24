# tic-tac-toe game for SkillFactory B5.6
helloText = """
***********************************************************************************************
*                                                                                             *
*     *******   *   *   *        *******     *      *    *        *******   ***    * * *      *
*        *      *   *  *            *       * *     *  *             *     *   *   *          *
*        *      *   * *    ****     *      * * *    * *     ****     *     *   *   * * *      *
*        *      *   *  *            *     *     *   *  *             *     *   *   *          *
*        *      *   *   *           *    *       *  *    *           *      ***    * * *      *
*                                                                                             *
***********************************************************************************************"""
gameRulesText = """
    Правила игры:
    Игроки поочередно вводят координаты клеток в формате XY (строка, столбец) и таким образом
    ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).
    Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали,
    выигрывает. Первый ходит крестик - 'X'."""
gameDesk = [[" ", " ", " "] for i in range(0, 3)]

#print(helloText)
#print(gameRulesText)
#input("\n               Нажмите 'Enter' чтобы продолжить...")


def drawGameDesk(gameDesk_):
    print()
    print("     |  " + "  |  ".join("123") + "  |")
    print("-----|" * 4)
    for i in range(0, 3):
        print(f"  {i+1}  |", end='')
        for j in range(0, 3):
            print(f"  {gameDesk_[i][j]}  |", end='')
        print("\n" + "-----|" * 4)
    print()

def isWin(gameDesk_):
    pass
    return 0

def getInput(char_, gameDesk_):

    while 1:
        print("\033[H\033[J")
        if char_ == 'X':
            print("Ходит 'крестик'...")
        else:
            print("Ходит 'нолик'...")

        drawGameDesk(gameDesk_)

        inputString = input("Введите координаты клетки в формате  XY (строка, столбец): ").replace(" ","")

        if not (len(inputString) == 2 and inputString.isdigit()):
            print("Неверный ввод. X и Y должны быть цыфрами от 1 до 3")
            continue

        x, y = map(int, inputString[0:])
        x -= 1
        y -= 1

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Координаты вне диапазона. Повторите ввод")
            continue

        if not gameDesk_[x][y] == " ":
            print("Клетка занята. Повторите ввод")
            continue

        return x, y




turn = 1
while turn < 10:

    if turn % 2:
        char_ = 'X'
    else:
        char_ = '0'

    x, y = getInput(char_, gameDesk)
    gameDesk[x][y] = char_



    turn += 1

