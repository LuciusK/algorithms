

from collections import defaultdict
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from loguru import logger


class NaiveBayesScratch():
    def __init__(self):
        # 先验概率P(Y|ck)
        self.prior_prob = defaultdict(float)
        # 似然概率
        self.likelihood = defaultdict(defaultdict)
        # 每个类别样本个数
        self.ck_counter = defaultdict(float)
        # 每维特征可能取值个数
        self.Sj = defaultdict(float)
    
    def fit(self, X, y):
        n_sample, n_feature = X.shape
        


def main():
    X, y = load_iris(return_X_y = True)
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size = 0.8, shuffle = True)

    model = 
    model.fit(xtrain, ytrain)

    n_test = xtest.shape[0]
    n_right = 0
    for i in range(n_test):
        y_pred = model.predict(xtest[i])
        if y_pred == ytest[i]:
            n_right += 1
        else:
            logger.info("该样本真实标签为：{},但是Scratch模型预测标签为:{}".format(ytest[i], y_pred))
    logger.info("Scratch模型在测试集上的准确率为:{}%".format(n_right * 100 / n_test))

if if __name__ == "__main__":
    main()