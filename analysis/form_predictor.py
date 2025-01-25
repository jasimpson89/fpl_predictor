import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px

import matplotlib.pyplot as plt

def fit_linear_regression(df):
    X = df[['fdr']].values.reshape(-1, 1)
    y = df['total_points'].values

    model = LinearRegression()
    model.fit(X, y)



    return model

def main(df):
    fx_model = fit_linear_regression(df)
    print(fx_model.coef_, fx_model.intercept_)

    
    df['total_points_pred'] = fx_model.predict(df['fdr'].values.reshape(-1, 1))

    return

   