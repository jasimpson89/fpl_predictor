import pandas as pd
import numpy as np
import create_player_pdf.plot_player_pdf as plot_pdf
from scipy.stats import gaussian_kde

import plotly.express as px
class player:
    def __init__(self, first_name, second_name, path_year, path_year_gw): #TODO expand this to allow for multiple years of data
        self.first_name = first_name
        self.second_name = second_name
        self.name = f"{first_name} {second_name}"

        # read all 2023 data
        df = pd.read_csv(path_year, header=0)
        self.df = df

        # read the game week data
        df_gw = pd.read_csv(path_year_gw, header=0)
        self.df_gw = df_gw

        print(self.name)
        print(self.df_gw)


        # locate the player data within the dataframes found
        self.df_player = self.get_player_data()

        # get now calculate the player pdf
        self.df_player_pdf = self.get_player_pdf()


    def get_player_data(self):

        df_player = (self.df_gw).loc[self.df_gw["name"]== self.name]
        print(df_player["total_points"])
        print(df_player["GW"])
        return df_player

    def get_player_pdf(self):
        # Get a PDF function using a Gaussian KDE



        df1 = self.df_player.set_index('name')
        dataset = df1['total_points'].to_numpy()

        pdf_kernal = gaussian_kde(dataset, bw_method=None, weights=None)
        x_axis = np.linspace(-dataset.max(), 10 + dataset.max())
        pdf = pdf_kernal(x_axis)

        df_pdf = pd.DataFrame(
            pdf,
            index=x_axis,
            columns=["pdf"]
        )

        return df_pdf


def make_player_obj(player_first_name,player_second_name, path_year, path_year_gw):


    player_ = player(player_first_name, player_second_name, path_year, path_year_gw)
    fig = plot_pdf.plot(player_)
    return player_ , fig
