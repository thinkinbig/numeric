import numpy as np
from util import is_regular


def backward_sub(R, y):
    assert is_regular(R)
    N = len(y)
    assert R[0] == N
    x = np.zeros(N)
    for n in range(N - 1, -1, -1):
        x[n] = (y[n] - np.dot(R[n, n: N], x[n: N])) / R[n, n]
    return x


def forward_sub(L, b):
    assert is_regular(L)
    N = len(b)
    assert L[0] == N
    y = np.zeros(N)
    for n in range(0, N):
        y[n] = (b[n] - np.dot(L[n, :n], y[:n])) / L[n, n]
    return y


def lr_decom(A):
    assert is_regular(A)
    N = len(A[0])
    L = np.eye(N)
    R = np.zeros(N)
    R[0][0] = A[0][0]
    for n in range(1, N):
        l21 = forward_sub(np.transpose(R[:n, :n]), A[n, :n])
        r12 = forward_sub(L[:n, :n], A[:n, n])
        r22 = A[n, n] - np.dot(l21, r12)
        # Assemble to L
        L[n, :n] = l21
        # Assemble to R
        R[:n, n] = r12
        R[n, n] = r22
    return L, R
