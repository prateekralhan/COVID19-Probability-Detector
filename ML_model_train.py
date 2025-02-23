import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')
import pickle



def data_split(data,ratio):
    np.random.seed(42)
    shuffled=np.random.permutation(len(data))
    test_set_size=int(len(data)*ratio)
    test_indices=shuffled[:test_set_size]
    train_indices=shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]


if __name__ == '__main__':
    df=pd.read_csv("data.csv")
    train,test= data_split(df,0.2)

    X_train=train[['fever','bodyPain','age','runnyNose','diffbreath']].to_numpy()
    X_test=test[['fever','bodyPain','age','runnyNose','diffbreath']].to_numpy()

    Y_train=train[['infectionProb']].to_numpy().reshape(8000,)
    Y_test=test[['infectionProb']].to_numpy().reshape(1999,)

    logreg=LogisticRegression()
    logreg.fit(X_train,Y_train)

    file=open('ml_model.pkl','wb')
    pickle.dump(logreg,file)
    file.close()
