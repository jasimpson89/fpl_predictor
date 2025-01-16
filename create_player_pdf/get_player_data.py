import pandas as pd
import numpy as np

from scipy.stats import gaussian_kde

import plotly.express as px

 
class player:
    def __init__(self, first_name, second_name, path_year, path_year_gw, path_raw, fixture_path): #TODO expand this to allow for multiple years of data
        self.first_name = first_name
        self.second_name = second_name
        self.name = f"{first_name} {second_name}"

        # read all 2023 data
        df = pd.read_csv(path_year, header=0)
        self.df = df

        # read the game week data
        df_gw = pd.read_csv(path_year_gw, header=0)
        self.df_gw = df_gw

        # print(self.name)
        # print(self.df_gw)


        # locate the player data within the dataframes found
        self.df_player = self.get_player_data()

        # get now calculate the player pdf
        self.df_player_pdf = self.get_player_pdf()

        # calc player form
        self.df_player  = self.calc_player_form()
  

        # read raw player data to get form 
        self.df_raw = pd.read_csv(path_raw, header=0)
        self.df_player_raw = self.df_raw.loc[(self.df_raw["first_name"]== self.first_name) & (self.df_raw["second_name"]== self.second_name)]

        # get fixture data
        self.df_player_fixtures = self.get_fixture_data(fixture_path)


    def calc_player_form(self):
        # calculate the form of a player, but as rolling average from df_player
        avg = self.df_player['total_points'].rolling(window=5, min_periods=5).mean()
        self.df_player.loc[:,'rolling_form'] = avg
        self.df_player.loc[self.df_player['GW'] < 5, 'rolling_form'] = np.nan
        return self.df_player
       
    def get_player_data(self):

        df_player = (self.df_gw).loc[self.df_gw["name"]== self.name]
        # print(df_player["total_points"])
        # print(df_player["GW"])
        return df_player

    def get_player_pdf(self):
        # Get a PDF function using a Gaussian KDE



        df1 = self.df_player.set_index('name')
        dataset = df1['total_points'].to_numpy()

        pdf_kernal = gaussian_kde(dataset, bw_method=None, weights=None)
        x_axis = np.linspace(-dataset.max(), 10 + dataset.max())
        pdf = pdf_kernal(x_axis)
        names = [self.name]*len(x_axis)
        # df_pdf = pd.DataFrame(
        #     [pdf, self.name],
        #     index=x_axis,
        #     columns=[self.name, "name"]
        #     # columns=["pdf"]
        # )

        df_pdf = pd.DataFrame(
            pdf,
            index=x_axis,
            columns=[self.name]
            # columns=["pdf"]
        )

        return df_pdf
    
    def get_fixture_data(self, fixture_path):
        # get the fixture data for the player
        fixtures_df = pd.read_csv(fixture_path)
        df_player = self.df_player
        # Merge player data with fixture data based on kickoff_time and team
        merged_df = pd.merge(df_player, fixtures_df, how='left', left_on=['kickoff_time', 'opponent_team'], right_on=['kickoff_time', 'team_a'])

        # Drop duplicate columns after merge
        merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

        # sort out fixture difficulty rating working out whether the fixture was at home or away for the player
        merged_df.loc[merged_df['at_home'] == True, 'fdr'] = merged_df['team_h_difficulty']
        merged_df.loc[merged_df['at_home'] == False, 'fdr'] = merged_df['team_a_difficulty']

        return merged_df



def make_player_obj(player_first_name,player_second_name, path_year, path_year_gw, path_player_raw):


    player_ = player(player_first_name, player_second_name, path_year, path_year_gw, path_player_raw)
    # fig = plot_pdf.plot(player_)
    return player_
