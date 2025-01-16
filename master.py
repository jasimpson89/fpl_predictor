import create_player_pdf.get_player_data as get_player_data
import plotly.express as px
from plotly.subplots import make_subplots
import plotting.plot_players_pdf as plot_players_pdf
import git
import analysis.form_predictor as form_predictor
def main():
    # g = git.cmd.Git('/data_fpl')
    # g.status()
    # g.pull()

    repo = git.Repo('./data_fpl')
    origin = repo.remote(name='origin')
    origin.pull()

    print('======== Checking status of FPL data ========')
    print(repo.git.status())
    print('=============================================')


    # TODO add this to json file, how are we going to look at historical data?
    path_2023 = "data_fpl/data/2023-24/cleaned_players.csv"
    path_2023_gw = "data_fpl/data/2023-24/gws/merged_gw.csv"
    path_2023_player_raw = "data_fpl/data/2023-24/players_raw.csv"
    path_2023_fixtures = "data_fpl/data/2023-24/fixtures.csv"

    # TODO make a JSON file to import player names and clubs
    player_first_names = ["Mohamed", "Erling"]
    player_second_names = ["Salah", "Haaland"]

    colors = ["red", "blue"]

    players = {} # dictionary of players
    # fig = make_subplots(rows=1, cols=2, start_cell="top-left")
    fig_form = make_subplots(rows=1, cols=1, start_cell="top-left")


    for first_name, second_name, color in zip(player_first_names, player_second_names, colors):
        player_ = get_player_data.make_player_obj(first_name,second_name,
                                                           path_2023, path_2023_gw, path_2023_player_raw, path_2023_fixtures)

        players[player_.name] = player_

        print(player_.name)
        print(player_.df_player["rolling_form"])

        # plot_players_pdf.plot(player_, fig_form, color=color)

        # form_predictor.test_bernoulli_predictor(player_.df_player, player_.name)

    

    # fig_pdf.show()
    fig_form.show()

main()
print('END')