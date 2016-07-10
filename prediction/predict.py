import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn import cross_validation


def days_between(d1, d2):
	d1 = datetime.strptime(d1, "%d/%m/%Y")
	d2 = datetime.strptime(d2, "%d/%m/%Y")
	return abs((d2-d1).days)


l_cat = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12}
l_days = []
cat = []


def scatter_plot(X,Y):
    plt.subplot(5,3,1)
    # columns = ['crim','zn','indus','chos','nox','rm','age','dis','rad','tax','ptratio','b','lstat']
    columns = ['cat', 'amount', 'days']
    subplot_counter = 1
    for c in range(len(columns)):
        x = X[c]
        y = Y
        plt.subplot(5,3,subplot_counter)
        plt.scatter(x,y)
        plt.axis("tight")
        # plt.title('Feature Selection', fontsize=14)
        plt.xlabel(columns[c], fontsize=12)
        plt.ylabel("price", fontsize=12)
        subplot_counter+=1
    plt.show()


def parameter_grid(X, z, Y):
    scoresCV = []
    scores = []
    for i in range(1,4):
        new_df=z[0:i]
        new_df = new_df.transpose()
        # X = new
        # X = new_df.ix[:,1::]
        # y = new_df.ix[:,0]
        clf = LinearRegression()
        scoreCV = cross_validation.cross_val_score(clf, new_df, Y, cv=3)
        # print new_df.head()
        # print np.mean(scoreCV)
        scores.append(np.mean(scoreCV))

    plt.figure(figsize=(15,5))
    plt.plot(range(1,len(scores)+1),scores, '.-')
    plt.axis("tight")
    plt.title('Feature Selection', fontsize=14)
    plt.xlabel('# Features', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.show()


def cleaning():
	df = pd.read_json('campaign_data.json')
	
	for i in range(1000):
		l_days.append(days_between(df['started'][i], df['ended'][i]))
		cat.append(l_cat[df['category'][i]])
	# print cat
	X = np.array([cat, df['pledged_amount'], l_days])
	Y = np.array([df['donation_received']])
	# scatter_plot(X, Y)
	X = preprocessing.scale(X)
	z = X
	Xtr = X.transpose()
	Ytr = Y.transpose()
	parameter_grid(Xtr, z, Ytr)
	predict(Xtr, Ytr)	



def predict(X, Y):
	# X = df[list(df.columns)[:-1]]
	# Y = df["quality"]
	# print X
	# print Y
	X_train,X_test,Y_train,Y_test = train_test_split(X,Y)
	# print X_train
	# print Y_train

	regressor = LinearRegression()
	regressor.fit(X_train,Y_train)

	scores = cross_val_score(regressor,X,Y,cv = 3)
	print scores.mean(),scores

	y_prediction = regressor.predict(X_test)

	print "r squared=",regressor.score(X_test,Y_test)
	print "abs error",median_absolute_error(Y_test,y_prediction)
	print "mean squared error",mean_squared_error(Y_test,y_prediction)


if __name__ == "__main__":
	cleaning()