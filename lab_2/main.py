import numpy as np

from lab_1 import main


def find_Q(z, x, B):
    Q = np.array([float('inf') if i <= 0 else x[B[ind] - 1] / i for ind, i in enumerate(z)])
    return min(Q)


def find_z(A_b, A, delta):
    j0, delta1 = [(i, value) for i, value in enumerate(delta) if value < 0][0]
    A_j0 = [A[i][j0] for i in range(len(A))]
    z = np.zeros(len(A_j0))

    for j in range(len(A_j0)):
        for i in range(len(A_j0)):
            z[i] += A_b[j][i] * A_j0[i]
    print(z, '\tvector z')
    return z


def grade_vector(u, A, c):
    delta = np.zeros(len(c))

    for j in range(len(c)):
        for i in range(len(u)):
            delta += u[i] * A[i][j]
    delta -= c
    print(delta)
    if all(map(lambda item: True if item >= 0 else False, delta)):
        raise ValueError('jsmpovjfdoij')
    return delta


def potential_vector(c, A_b, B):
    c_b = [c[i - 1] for i in B if i in B]
    u = np.zeros(len(c_b))
    for j in range(len(c_b)):
        for i in range(len(c_b)):
            u[j] += c_b[i] * A_b[i][j]
    print(u, '\tpotential vector u: ')
    print()
    return u


def find_reversed_A(A, B: list[int]):
    A_b = np.zeros(len(B) ** 2).reshape(len(B), len(B))
    for indx, column in enumerate(B):
        A_b[indx] = [A[indx][i - 1] for i in B if i in B]
    print(np.linalg.inv(A_b), '\tA ** -1: ')
    print()
    return np.linalg.inv(A_b)


if __name__ == '__main__':
    A = np.array([[-1, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]])
    B = [3, 4, 5]
    c = np.array([1, 1, 0, 0, 0])
    x = [0, 0, 1, 3, 2]
    A_b = find_reversed_A(A, B)
    u = potential_vector(c, A_b, B)
    delta = grade_vector(u, A, c)
    z = find_z(A_b, A, delta)
    Q = find_Q(z, x, B)
    print(Q)