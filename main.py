# tic-tac-toe game for SkillFactory B5.6
import os

hello_text = """
***********************************************************************************************
*                                                                                             *
*     *******   *   *   *        *******     *      *    *        *******   ***    * * *      *
*        *      *   *  *            *       * *     *  *             *     *   *   *          *
*        *      *   * *    ****     *      * * *    * *     ****     *     *   *   * * *      *
*        *      *   *  *            *     *     *   *  *             *     *   *   *          *
*        *      *   *   *           *    *       *  *    *           *      ***    * * *      *
*                                                                                             *
***********************************************************************************************"""
rule_text = """
    Правила игры:
    Игроки поочередно вводят координаты клеток в формате XY (строка, столбец) и таким образом
    ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).
    Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали,
    выигрывает. Первый ходит крестик - 'X'."""

# Заполняем клетки пробелами
gamedesk = [[" ", " ", " "] for i in range(0, 3)]

# Отрисовка игрового поля
def draw_gamedesk(gamedesk_):
    #print("\n\n")
    print()
    print()
    print("     |  " + "  |  ".join("123") + "  |")
    print("-----|" * 4)
    for i in range(0, 3):
        print(f"  {i + 1}  |", end='')
        for j in range(0, 3):
            print(f"  {gamedesk_[i][j]}  |", end='')
        print("\n" + "-----|" * 4)
    print()


# Проверка на выигрышную комбинацию
def is_win(char_):
    win_states = (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),
                ((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0)))

    for state in win_states:
        captured_cells = 0
        for x, y in state:
            if gamedesk[x][y] == char_:
                captured_cells += 1
            else:
                break
        if captured_cells == 3:
            return True
    return False


# Ввод координат клетки и их валидация
def get_input(char_):

    while 1:
        in_string = input("Введите координаты клетки в формате  XY (строка, столбец): ").replace(" ","")

        if not (len(in_string) == 2 and in_string.isdigit()):
            print("Неверный ввод. X и Y должны быть цыфрами от 1 до 3")
            continue

        x, y = map(int, in_string)
        x -= 1
        y -= 1

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Координаты вне диапазона. Повторите ввод")
            continue

        if not gamedesk[x][y] == " ":
            print("Клетка занята. Повторите ввод")
            continue

        return x, y


# Очистка экрана, отображение правил игры
os.system('cls||clear')
print(hello_text)
print(rules_text)
input("\n               Нажмите 'Enter' чтобы продолжить...")
os.system('cls||clear')
draw_gamedesk(gamedesk)
turn = 0

while turn < 9:
    turn += 1
    if turn % 2:
        char_ = 'X'
        print("Ходит 'крестик'...")
    else:
        char_ = '0'
        print("Ходит 'нолик'...")

    x, y = get_input(char_)
    gamedesk[x][y] = char_
    os.system('cls||clear')
    draw_gamedesk(gameDesk)

    if is_win(char_):
        print("   **************")
        print(f"   * Победил {char_}! *")
        print("   **************")
        break

    if turn == 9:
        print("   **************")
        print("   *   Ничья!   *")
        print("   **************")

