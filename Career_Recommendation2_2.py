#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

df2=pd.read_csv('pro.csv')
df2= df2.iloc[:,1:]
df10= df2.iloc[:,:7].join(df2.iloc[:,23:25]).join(df2.iloc[:,26:27]).join(df2.iloc[:,33:34]).join(df2.iloc[:,-1:]) 

from sklearn.utils import shuffle
df = shuffle(df10)
df= df.dropna()

fitdf= pd.DataFrame(df10.iloc[:,:17])

fitdf.head(2)

from sklearn.preprocessing import LabelEncoder
label_encoder = preprocessing.LabelEncoder()
df['Interested subjects']= label_encoder.fit_transform(df['Interested subjects'])
df['Interested subjects'].unique()

label_encoder2 = preprocessing.LabelEncoder()
df['interested career area']= label_encoder2.fit_transform(df['interested career area'])
df['interested career area'].unique()

label_encoder3 = preprocessing.LabelEncoder()
df['Suggested Job Role']= label_encoder3.fit_transform(df['Suggested Job Role'])
df['Suggested Job Role'].unique()

label_encoder3 = preprocessing.LabelEncoder()
df['Type of company want to settle in?']= label_encoder3.fit_transform(df['Type of company want to settle in?'])
df['Type of company want to settle in?'].unique()

label_encoder4 = preprocessing.LabelEncoder()
df['Management or Technical']= label_encoder4.fit_transform(df['Management or Technical'])
df['Management or Technical'].unique()

df.iloc[:,:].head(2)

train= df[:df.shape[0]*80//100].dropna()
test= df[df.shape[0]*80//100:].dropna()

X_test= test.iloc[:, :-1]
X_train= train.iloc[:, :-1]
y_test= test.iloc[:,-1:]
y_train= train.iloc[:,-1:]



X_train= np.array(X_train)
X_test= np.array(X_test)
y_train= np.array(y_train)
y_test= np.array(y_test)

from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors= 10)
knn.fit(X_train, y_train)
knn.score(X_test,y_test)*100

jobs= (df2[df.columns[-1]]).tolist()

lul= int(np.floor(np.random.rand()*17217))
live= df.iloc[lul:lul+2, :-1]

import mysql.connector

mydb =  mysql.connector.connect(host="localhost",user="root",passwd="",database="carrier")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM subjects")

result = mycursor.fetchall()

res0 = result[0][0]
res1 = result[0][1]
res2 = result[0][2]
res3 = result[0][3]
res4 = result[0][4]
res5 = result[0][5]
res6 = result[0][6]
res7 = result[0][7]
res8 = result[0][8]
res9 = result[0][9]
res10 =  result[0][10]


tl=[res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10]
live= pd.concat([live, pd.DataFrame([tl], columns= df.columns[:-1])], sort=False)

live_df= live.iloc[:, :8]
for i, e in enumerate(live.columns[:]):
    if live.dtypes[i] == 'O':
        live_df[live.columns[i]]= live[live.columns[i]].astype('category').cat.codes
know= ((knn.predict(live_df)))[2]
print("Suggested Career Path: "+jobs[know])

mycursor.execute("""INSERT INTO `job` (`JOB`) VALUE ('%s')""" % (jobs[know]))
mydb.commit()


# In[7]:


#lul= int(np.floor(np.random.random()*17217))
#np.array(df1.iloc[lul, 1:-1])


# In[ ]:
