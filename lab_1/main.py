import numpy as np


def step_1(A_reversed: np.array, X: np.array):
    L = np.zeros(X.size)
    for row in A_reversed:
        for x, column in zip(X, range(len(X))):
            L[column] += row[column] * x
    print(L)
    return L


def step_2(L: np.array, i: int):
    L_temp = L.copy()
    L_temp[i - 1] = -1
    print(L_temp)
    return L_temp


def step_3(L: np.array, temp_L: np.array, i: int):
    hatted_L = -1 / L[i - 1] * temp_L
    print(hatted_L)
    return hatted_L


def step_4(hatted_L: np.array, i: int):
    Q = np.eye(hatted_L.size)
    j = 0
    for row in Q:
        row[i - 1] = hatted_L[j]
        j += 1
    print('Q', Q)
    return Q


def step_5(Q: np.array, A_reversed: np.array, i: int):
    j = 0
    result_A = np.zeros(i)





def find_reversed_matrix(A: np.array,  A_reversed: np.array, X: np.array, i: int):
    A_temp = A.copy()
    for row, x in zip(A_temp, X):
        row[i - 1] = x
    print(A_temp)
    L = step_1(A_reversed, X)
    if L[i - 1] == 0:
        return 'Matrix is irreversible'
    temp_L = step_2(L, i)
    hatted_L = step_3(L, temp_L, i)
    Q = step_4(hatted_L, i)
    print('step 5', step_5(Q, A_reversed, i))


if __name__ == '__main__':
    A = np.array([[1, -1, 0], [0, 1, 0], [0, 0, 1]])
    A_reversed = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    X = np.array([1, 0, 1])
    find_reversed_matrix(A, A_reversed, X, 3)
