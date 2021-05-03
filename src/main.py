import numpy as np
from linear import linear_algo as lr

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = np.array([[1, 4, -1], [3, 0, 5], [2, 2, 1]])
    L, R = lr.lr_decom(A)
    print(L)
    print(R)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
