
from collections import defaultdict
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from loguru import logger


class NaiveBayesScratch:
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
        ck, num_ck = np.unique(y, return_counts=True)
        self.ck_counter = dict(zip(ck, num_ck))
        for label, num_label in self.ck_counter.items():
            self.prior_prob[label] = (num_label + 1) / (n_sample + ck.shape[0])

        # 记录每个类别对应的索引
        ck_idx = list()
        for label in ck:
            label_idx = np.squeeze(np.argwhere(y == label))
            ck_idx.append(label_idx)

        # 遍历每一个标签
        for label, idx in zip(ck, ck_idx):
            xdata = X[idx]

            # 记录该类别所有特征对应的概率
            label_likelihood = defaultdict(defaultdict)
            # 遍历每一维特征
            for i in range(n_feature):
                # 记录该特征每一个取值对应的概率
                feature_val_prob = defaultdict(float)
                # 获取该列特征可能的取值和每个值出现的次数
                feature_val, feature_cnt = np.unique(xdata[: i], return_counts=True)
                self.Sj[i] = feature_val.shape[0]
                for fea_val, cnt in zip(feature_val, feature_cnt):
                    feature_val_prob[fea_val] = (cnt + 1) / (self.ck_counter[label] + self.Sj[i])
                label_likelihood[i] = feature_val_prob
            self.likelihood[label] = label_likelihood

    def predict(self, x):
        




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

if __name__ == "__main__":
    main()