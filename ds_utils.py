
def dropcolumns(df):
    df = df.copy()
    df= df.drop(columns=[drop_clomuns])
 return X



def splitter(df):
    train, test =  train_test_split(df, train_size=.8)
    train, val = train_test_split(train, train_size=.8)
print(train, test, val)



def null(X):
 null_list = X.isnull().sum()
 return null_list
