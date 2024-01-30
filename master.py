import create_player_pdf.get_player_data as get_player_data
import plotly.express as px
from plotly.subplots import make_subplots
import plotting.plot_players_pdf as plot_players_pdf
import git
if __name__ == '__main__':
    # g = git.cmd.Git('/Fantasy-Premier-League')
    # g.status()
    # g.pull()

    repo = git.Repo('./Fantasy-Premier-League')
    origin = repo.remote(name='origin')
    origin.pull()

    print('======== Checking status of FPL data ========')
    print(repo.git.status())
    print('=============================================')


    # TODO add this to json file, how are we going to look at historical data?
    path_2023 = "Fantasy-Premier-League/data/2023-24/cleaned_players.csv"
    path_2023_gw = "Fantasy-Premier-League/data/2023-24/gws/merged_gw.csv"

    # TODO make a JSON file to import player names and clubs
    player_first_names = ["Mohamed", "Erling"]
    player_second_names = ["Salah", "Haaland"]



    players = {} # dictionary of players
    fig = make_subplots(rows=1, cols=2, start_cell="top-left")


    for first_name, second_name in zip(player_first_names, player_second_names):
        player_ = get_player_data.make_player_obj(first_name,second_name,
                                                           path_2023, path_2023_gw)

        players[player_.name] = player_

        fig_pdf = plot_players_pdf.plot(player_, fig)

    fig_pdf.show()