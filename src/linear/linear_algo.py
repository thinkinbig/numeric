import numpy as np

import util
from numpy import linalg as la


def backward_sub(R, y):
    assert util.is_regular(R)
    N = len(y)
    x = np.zeros(N)
    for n in range(N - 1, -1, -1):
        x[n] = (y[n] - np.dot(R[n, n: N], x[n: N])) / R[n, n]
    return x


def forward_sub(L, b):
    assert util.is_regular(L)
    N = len(b)
    y = np.zeros(N)
    for n in range(0, N):
        y[n] = (b[n] - np.dot(L[n, :n], y[:n])) / L[n, n]
    return y


def lr_decom(A):
    assert util.is_regular(A)
    N = A.shape[0]
    L = np.eye(N)
    R = np.zeros(A.shape)
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


def cholesky(A):
    assert util.is_positive_definite(A)
    assert util.is_symmetric(A)
    N = A.shape[0]
    L = np.zeros(A.shape)
    L[0, 0] = np.sqrt(A[0, 0])
    for n in range(1, N):
        y = forward_sub(L[:n, :n], A[n, :n])
        # Assemble to L
        L[n, :n] = y
        L[n, n] = np.sqrt(A[n, n] - np.dot(y, y))
    return L


def householder(v):
    N = v.shape[0]
    delta = -la.norm(v, 2) if v[0] > 0 else la.norm(v, 2)
    e1 = np.zeros(N)
    e1[0] = 1
    # normalize the w
    w = util.normalize(v - delta * e1)
    # np.identity(N) - 2 * np.multiply(w, w.reshape(-1, 1)) Matrix from Householder Transformation
    return w


def qr_decom(A):
    N = A.shape[0]
    Q = np.identity(N)
    for i in range(0, N):
        a1 = A[i:N, i]
        w1 = np.pad(householder(a1), (i, 0), 'constant', constant_values=0)
        Q1 = np.identity(N) - 2 * np.multiply(w1, w1.reshape(-1, 1))
        A = Q1.dot(A)
        Q = Q.dot(Q1)
    return Q, np.multiply(Q, A)
