from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR: Path = Path(__file__).parent.parent

if __name__ == '__main__':
    path_2023_gw = DATA_DIR / "Fantasy-Premier-League" / "data" / "2023-24" / "gws" / "merged_gw.csv"

    # loads in all game week data for the year
    df_gw = pd.read_csv(path_2023_gw, header=0)

    # filter df down to just what we need: name, total_points, game week
    columns = ["name", "total_points", "GW"]
    df_all_players = df_gw.loc[:,columns]


    # df_player = (self.df_gw).loc[self.df_gw["name"] == self.name]

    player_first_name = "Mohamed"
    player_second_name = "Salah"
    player_name = f"{player_first_name} {player_second_name}"

    # This sets the
    print(
        df_all_players.set_index('name').loc[player_name, 'total_points'].head()
    )

    # this produces the histogram of the players points
    # i.e. the count a number of points occues of the numbers of points
    df_all_players.set_index('name').loc[player_name, 'total_points'].hist()  # xlabel="Total Points", ylabel="Count (of that value of point)")
    # Plot the total points vs game week for Saleh
    df_all_players.set_index('name').loc[player_name].set_index('GW').plot()


    # Get a PDF function using a Gaussian KDE
    from scipy.stats import gaussian_kde

    # Time dependent prediction using Gaussian Processes
    df1 = df_all_players.set_index('name')
    dataset = df1[df1['GW'] < 14]['total_points'].to_numpy()
    dataset0 = df1[df1['GW'] < 14]['total_points'].to_numpy()

    pdf_kernal = gaussian_kde(dataset, bw_method=None, weights=None)
    x_axis = np.linspace(-10, 10 + dataset.max())
    pdf = pdf_kernal(x_axis)

    df_pdf = pd.DataFrame(
        pdf,
        index=x_axis
    )
    df_pdf.plot()

    # Gaussian Processes

    pass