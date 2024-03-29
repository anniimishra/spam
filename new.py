import pandas as pd
message = pd.read_csv('SMSSpamCollection',sep='\t',names=["label","message"])
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
corpus=[]
for i in range(0,len(message)):
    review=re.sub('[^a-zA-Z^]',' ',message['message'][i])
    review=review.lower()
    review=review.split()
    review={ps.stem(word) for word in review if not word in stopwords.words('english')}
    review=' '.join(review)
    corpus.append(review)
    from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()
y=pd.get_dummies(message['label'])
y=y.iloc[:,1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB().fit(X_train,y_train)
y_pred=model.predict(X_test)