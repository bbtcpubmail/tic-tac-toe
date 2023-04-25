# tic-tac-toe game for SkillFactory B5.6
import os

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

# Заполняем клетки пробелами
gameDesk = [[" ", " ", " "] for i in range(0, 3)]

# Отрисовка игрового поля
def drawGameDesk(gameDesk_):
    #print("\n\n")
    print()
    print()
    print("     |  " + "  |  ".join("123") + "  |")
    print("-----|" * 4)
    for i in range(0, 3):
        print(f"  {i+1}  |", end='')
        for j in range(0, 3):
            print(f"  {gameDesk_[i][j]}  |", end='')
        print("\n" + "-----|" * 4)
    print()


# Проверка на выигрышную комбинацию
def isWin(char_):
    winStates = (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),
    ((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0)))

    for state in winStates:
        capturedCells = 0
        for x, y in state:
            if gameDesk[x][y] == char_:
                capturedCells += 1
            else:
                break
        if capturedCells == 3:
            return True
    return False


# Ввод координат клетки и их валидация
def getInput(char_):

    while 1:

        inString = input("Введите координаты клетки в формате  XY (строка, столбец): ").replace(" ","")

        if not (len(inString) == 2 and inString.isdigit()):
            print("Неверный ввод. X и Y должны быть цыфрами от 1 до 3")
            continue

        x, y = map(int, inString)
        x -= 1
        y -= 1

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Координаты вне диапазона. Повторите ввод")
            continue

        if not gameDesk[x][y] == " ":
            print("Клетка занята. Повторите ввод")
            continue

        return x, y


# Очистка экрана, отображение правил игры
os.system('cls||clear')
print(helloText)
print(gameRulesText)
input("\n               Нажмите 'Enter' чтобы продолжить...")
os.system('cls||clear')
drawGameDesk(gameDesk)
turn = 0
while turn < 9:
    turn += 1
    if turn % 2:
        char_ = 'X'
        print("Ходит 'крестик'...")
    else:
        char_ = '0'
        print("Ходит 'нолик'...")

    x, y = getInput(char_)

    gameDesk[x][y] = char_
    os.system('cls||clear')
    drawGameDesk(gameDesk)

    if isWin(char_):
        print("   **************")
        print(f"   * Победил {char_}! *")
        print("   **************")
        break

    if turn == 9:
        print("   **************")
        print("   *   Ничья!   *")
        print("   **************")

