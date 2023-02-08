

import numpy as np
import pandas as pd


# In[4]:


df=pd.read_csv("C:/Users/Neelima/OneDrive/Desktop/stress(1).csv")
df.head()


# In[5]:


df.describe()


# In[6]:


df.isnull()


# In[7]:


df.isnull().sum()


# In[8]:


import nltk
import re
from nltk.corpus import stopwords
import string
nltk.download('stopwords')
stemmer=nltk.SnowballStemmer("english")
stopword=set(stopwords.words("english"))
def clean(text):
    text=str(text).lower()
    text=re.sub("\[.*?\]"," ",text)
    text=re.sub("https?://\S+/www\. \S+"," ",text)
    text=re.sub("<. *?>+"," ",text)
    text=re.sub('[%s]' %re.escape(string.punctuation)," ",text)
    text=re.sub(' \n'," ",text)
    text=re.sub("\w*\d\w*"," ",text)
    text=[word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text=[stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
df["text"]=df["text"].apply(clean)


# In[13]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

x=np.array(df["text"])
y=np.array(df["label"])

cv=CountVectorizer()
X=cv.fit_transform(x)
print(X)
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.33)


# In[10]:


from sklearn.naive_bayes import BernoulliNB
model=BernoulliNB()
model.fit(xtrain,ytrain)


# In[18]:


user=input("Enter the text")
data=cv.transform([user]).toarray()
output=model.predict(data)
print(output)


# In[ ]:




