import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report

df = pd.read_csv('/Users/duncan/Documents/programming/Python/myPyCharm/week11_diabetes/diabetes.csv')
# print(df.head())
# print(df.info())
feature_cols = ["glucose", "age", "insulin", "bmi", "pregnant", "pedigree", "bp"]
df.hist()

# X = df[feature_cols]  # features or independent variable
# y = df.label          # target variable/dependent variable
# # need to now get a train and test data set
# # we need to train a model on a test data set
#
# # 80% of data should be used for training (training helps the model understandthe data)
# # 20% of data should be used for testing (compare how accurate model is)
#
# # we use "train_test_split" from sklearn.model_selection
#
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
#
# logreg = LogisticRegression()
#
# # now fit the model to the data
# logreg.fit(X_train, y_train)
#
# y_pred = logreg.predict(X_test)
#
# cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
# print(cnf_matrix)
#
#
# print(pd.DataFrame(y_test).value_counts())
#
# print(pd.DataFrame(y_pred).value_counts())
#
# print(classification_report(y_test, y_pred))
#
# print(metrics.recall_score(y_test, y_pred))



