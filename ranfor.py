import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
import pickle

train1 = pd.read_csv('inl1.csv')
train2 = pd.read_csv('inr1.csv')

lis = []
for x in train2:
    train1[x]=train2[x]

train =train1
labs = pd.read_csv('out.csv')
print train.shape
print labs.shape
print 'Loading Model'

# clf= svm.SVC()
clf = RandomForestClassifier()
clf_ = svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None)
# pca = PCA(n_components = 3 )
# pca.fit(train)
# tran_data =pca.transform(train)
trainx,testx,trainy,testy = train_test_split(train,labs,train_size = 0.6,random_state =1)
clf.fit(trainx,trainy)
print(clf.score(testx,testy))
filename = 'gaze_model.sav'
pickle.dump(clf, open(filename, 'wb'))


# predict mein test data input hoga
# test data ka format train_data wala hi hoga
