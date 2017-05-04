
# coding: utf-8

# In[27]:

import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split


# In[10]:

train1 = pd.read_csv('/home/mohitrbhardwaj/Downloads/inl1.csv')
train2 = pd.read_csv('/home/mohitrbhardwaj/Downloads/inr1.csv')


# In[14]:

lis = []
for x in train2:
    train1[x]=train2[x]


# In[24]:

train1.shape


# In[22]:

train =train1


# In[19]:

labs = pd.read_csv('/home/mohitrbhardwaj/Downloads/oue.csv')


# In[32]:

clf= svm.SVC()


# In[25]:

clf.fit(train[:1000],labs[:1000])


# In[26]:

clf.score(train[1001:],labs[1001:])


# In[30]:

trainX, testX, trainY, testY = train_test_split(train, labs, train_size=0.7, random_state=42)


# In[31]:

trainX.shape


# In[33]:

clf.fit(trainX,trainY)


# In[34]:

clf.score(testX,testY)


# In[35]:

outpu = clf.predict(testX)


# In[39]:

# predict mein test data input hoga 
# test data ka format train_data wala hi hoga


# In[ ]:



