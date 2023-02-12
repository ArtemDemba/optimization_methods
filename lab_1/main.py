import numpy as np


def step_1(A_reversed: np.array, X: np.array):
    L = np.zeros(X.size)
    print(A_reversed, '\t- A_reversed')
    for row_indx, row in enumerate(A_reversed):      # находим матрицу l
        for x, column in zip(X, range(len(X))):
            L[row_indx] += row[column] * x

    print(L, '\t\t-\tstep 1')
    print()
    return L


def step_2(L: np.array, i: int):
    L_temp = L.copy()
    L_temp[i - 1] = -1      # заменяем i-й элемент в l на -1
    print(L_temp, '\t-\tstep 2')
    print()
    return L_temp


def step_3(L: np.array, temp_L: np.array, i: int):
    hatted_L = -1 / L[i - 1] * temp_L   # находим l с крышкой по формуле
    print(hatted_L, '\t-\tstep 3')
    print()
    return hatted_L


def step_4(hatted_L: np.array, i: int):
    Q = np.eye(hatted_L.size)           # генерируем единичную матрицу нужного размера
    j = 0
    for row in Q:                       # заменяем i-й столбец в единичной матрице на l с крышкой
        row[i - 1] = hatted_L[j]
        j += 1
    print(Q, '\t-\tstep 4')
    print()
    return Q


def step_5(Q: np.array, A_reversed: np.array, i: int):
    result_A = np.zeros((len(A_reversed), len(A_reversed))) # генерируем пустую матрицу, в которую будем
                                                            # записывать результат

    for row_index, row in enumerate(Q):         # заполняем по формуле, чтоб сложность была не O(n ^ 3), а O(n ^ 2)
        for column in range(len(A_reversed)):
            expression = Q[row_index][row_index] * A_reversed[row_index][column] + \
                         Q[row_index][i - 1] * A_reversed[i - 1][column]
            result_A[row_index][column] = expression / 2 if row_index == i - 1 else expression

    print(result_A, '\t-\tStep 5')
    print()
    return result_A


def find_reversed_matrix(A: np.array,  A_reversed: np.array, X: np.array, i: int):
    A_temp = A.copy()
    for row, x in zip(A_temp, X):   # заменяем i-й столбец на X
        row[i - 1] = x
    print(A_temp, '\t-\tafter exchanging i-th column in A')
    print()
    L = step_1(A_reversed, X)

    if L[i - 1] == 0:       # проверка: если i-й элемент в l равен 0, то матрица необратима
        raise ValueError('Matrix is irreversible')

    temp_L = step_2(L, i)
    hatted_L = step_3(L, temp_L, i)
    Q = step_4(hatted_L, i)

    return step_5(Q, A_reversed, i)


if __name__ == '__main__':
    A = np.array([[1, -1, 0], [0, 1, 0], [0, 0, 1]])
    A_reversed = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    X = np.array([1, 0, 1])
    i = 3
    try:
        find_reversed_matrix(A, A_reversed, X, i)
    except ValueError:
        print('Matrix is irreversible')
