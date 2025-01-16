import numpy as np
import pandas as pd
import plotly.express as px

def bernoulli_predictor(df_player, length):
    """
    Generates an array of True/False values based on a Bernoulli distribution
    using the rolling_average column to determine the probability.

    Parameters:
    df_player (pd.DataFrame): DataFrame containing the rolling_average column.
    length (int): The length of the resulting array.

    Returns:
    np.ndarray: An array of True/False values.
    """
    probabilities = df_player["rolling_form"].apply(lambda x: 0 if x < 2 else 0.5 if x < 6 else 0.8)
    return np.random.binomial(1, probabilities, length).astype(bool)

def test_bernoulli_predictor(df_player, player_name):
    length = len(df_player["GW"])
    result = bernoulli_predictor(df_player, length)
    df_result = pd.DataFrame({"GW": df_player["GW"], "Prediction": result})
    fig = px.histogram(df_result, x="GW", color="Prediction", barmode="group", title=str(player_name) + " Bernoulli Predictor Distribution")
    fig.show()

