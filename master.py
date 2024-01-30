import create_player_pdf.get_player_data as get_player_data
import plotly.express as px

if __name__ == '__main__':


    # TODO add this to json file, how are we going to look at historical data?
    path_2023 = "Fantasy-Premier-League/data/2023-24/cleaned_players.csv"
    path_2023_gw = "Fantasy-Premier-League/data/2023-24/gws/merged_gw.csv"

    # TODO make a JSON file to import player names and clubs
    player_first_name = "Mohamed"
    player_second_name = "Salah"


    players = {} # dictionary of players
    player_, fig_pdf = get_player_data.make_player_obj(player_first_name,player_second_name,
                                                       path_2023, path_2023_gw)

    players[player_.name] = player_

    fig_pdf.show()