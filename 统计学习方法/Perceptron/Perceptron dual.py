from Perceptron.perceptron base import PerceptronBase
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


class PercpetronDual(PerceptronBase):
    """
    感知机对偶形式
    """
    def __init__(self, eta = 0.1, n_iter = 50):
        super(PercpetronDual, self).__init__(eta = eta, n_iter = n_iter)

    #计算Gram Matrix
    def calculate_g_matrix(self, X):
        n_sample = X.shape[0]
        self.G_matrix = np.zeros((n_sample, n_sample))
        #填充Gram Matrix
        for i in range(n_sample):
            for j in range(n_sample):
                self.G_matrix[i][j] = np.sum(X[i] * X[j])
    
    #迭代的判定条件
    def judge(self, X, y, index):
        tmp = self.b
        n_sample = X.shape[0]
        for m in range(n_sample):
            tmp += self.alpha[m] * y[m] * self.G_matrix[index][m]
        
        return tmp * y[index]
    
    def fit(self, X, y):
        """
        由于对偶形式中训练实例仅以內积的形式出现
        因此，若事先求出Gram Matrix，能大大减少计算量
        """
        n_sample, n_features = X.shape
        self.alpha, self.b = [0] * n_sample, 0
        self.w = np.zeros(n_features)
        #计算Gram Matrix
        self.calculate_g_matrix(X)

        i = 0
        while i < n_sample:
            if self.judge(X, y, i) <= 0:
                self.alpha[i] += self.eta
                self.b += self.eta * y[i]
                i = 0
            else:
                i += 1
        
        for j in range(n_sample):
            self.w += self.alpha[j] * X[j] * y[j]

        return self


def main():
    iris = load_iris()
    X = iris.data[:100, [0, 2]]
    y = iris.target[:100]
    y = np.where(y == 1, 1, -1)
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size = 0.3)
    ppn = PercpetronDual(eta = 0.1, n_iter = 10)
    ppn.fit(X_train, y_train)


if __name__ == "__main__":
    main()