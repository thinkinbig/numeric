import numpy as np


def is_regular(M):
    return M.shape[0] == M.shape[1]


def is_positive_definite(M):
    return np.all(np.linalg.eigvals(M) > 0)


def is_symmetric(M):
    return np.transpose(M) == M


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm