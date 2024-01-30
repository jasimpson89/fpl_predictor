import plotly.express as px
from plotly.subplots import make_subplots

"""
player: object

return figure object for plotly 
"""
def plot(player):

    df_player = player.df_player
    df_player_pdf = player.df_player_pdf

    fig = make_subplots(rows=1,cols=2, start_cell = "top-left")

    # plot the histogram of points
    fig_histogram_bps = px.histogram(df_player, x="total_points")
    fig.add_trace(fig_histogram_bps.data[0], row=1,col=1)

    # plot the pdf
    fig_time_series_bps = px.line(df_player_pdf, y="pdf")
    fig.add_trace(fig_time_series_bps.data[0], row=1,col=2) # figure out how to set legend......





    return fig