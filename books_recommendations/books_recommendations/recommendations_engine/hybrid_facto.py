import numpy as np
import surprise
import pickle
import os

class HybridFacto(surprise.AlgoBase):

    def __init__(self, estimators=None, epochs=10, learning_rate=.05, q=4):
        if estimators is None:
            self.__stub_mode = True
            return
        self.alpha = np.array([1 / q] * q)
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.collabKNN = estimators[0]
        self.funkSVD = estimators[1]
        self.coClus = estimators[2]
        self.slopeOne = estimators[3]
        self.__stub_mode = False

    def fit(self, train_set):
        holdout = train_set.build_full_trainset().build_testset()
        predictions = []
        predictions.append(self.collabKNN.test(holdout))
        predictions.append(self.funkSVD.test(holdout))
        predictions.append(self.coClus.test(holdout))
        predictions.append(self.slopeOne.test(holdout))
        for epoch in range(self.epochs):
            maeGradient = np.array([surprise.accuracy.mae(prediction) for prediction in predictions])
            newalpha = self.alpha - maeGradient * self.learning_rate
            # проверка сходимости:
            if (newalpha - self.alpha).max() < 0.001:
                break
            self.alpha = newalpha

    def estimate(self, testset):
        if self.__stub_mode:
            return [0.0]
        algoResults = [np.array([i.est for i in self.collabKNN.test(testset)]),
                       np.array([i.est for i in self.funkSVD.test(testset)]),
                       np.array([i.est for i in self.coClus.test(testset)]),
                       np.array([i.est for i in self.slopeOne.test(testset)])]
        return self.alpha @ algoResults

    def dump_instance(self, dump_path):
        with open(dump_path, 'wb') as dump_file:
            pickle.dump(self, dump_file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_instance_from_dump():
        dump_path = './recommender.pkl'
        if os.path.exists(dump_path):
            with open(dump_path, 'rb') as dump_file:
                print('Loading dump starting')
                return pickle.load(dump_file)
        else:
            return HybridFacto()