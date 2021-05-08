import numpy as np
from linear import linear_algo as lr

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v = np.array([1, 2, 3])
    w = lr.householder(v)
    A = np.array([[1, 2, 3],
                  [2, 5, 0],
                  [3, 0, 4]])
    Q, R = lr.qr_decom(A)
    print(Q)
    print(R)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
