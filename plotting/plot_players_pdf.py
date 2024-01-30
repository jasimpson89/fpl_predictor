import plotly.express as px
from plotly.subplots import make_subplots

"""
player: object

return figure object for plotly 
"""


def plot(player, fig):
    df_player = player.df_player
    df_player_pdf = player.df_player_pdf

    # plot the histogram of points
    # fig_histogram_bps = px.histogram(df_player, x="total_points")
    # fig.add_trace(fig_histogram_bps.data[0], row=1,col=1)

    # Scatter plot of game weeks versus points
    fig_points = px.scatter(df_player, x='GW', y="total_points", color="name")
    fig.add_traces(fig_points.data)#, row=1, col=1)

    # plot the pdf
    # fig_time_series_bps = px.line(df_player_pdf, y=player.name)#, color="name")  # player.name)# + " pdf")
    # fig.add_traces(fig_time_series_bps.data)#, row=1, col=2)  # figure out how to set legend......

    return fig