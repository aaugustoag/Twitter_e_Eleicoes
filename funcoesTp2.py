import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# the dataset
df_tweets = pd.read_csv("pocketDF.csv")
df_tweets.drop(df_tweets[df_tweets.created_at < "2017-02-11"].index, inplace=True)
dataset = df_tweets.values

# input (X) and output (y)
X = dataset[:,2:18]
y = dataset[:,18]

# define model
def dnn_model():
    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=16, kernel_initializer='normal', activation='tanh'))
    # model.add(Dense(20, kernel_initializer='normal', activation='tanh'))
    model.add(Dense(1, kernel_initializer='normal', activation='linear'))
    # compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


# def results(dnn_model=dnn_model, X=X, y=y):
#     estimators = []
#     estimators.append(('standardize', StandardScaler()))
#     estimators.append(('mlp', KerasRegressor(build_fn=dnn_model, epochs=100, batch_size=100, verbose=1)))
#     pipeline = Pipeline(estimators)
#     kfold = KFold(n_splits=5, random_state=42)
#     return cross_val_score(pipeline, X, y, cv=kfold)


def r2(result, y=y):
    return 1 + result.mean()/((y - y.mean())**2).mean()
