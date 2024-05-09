from branca.colormap import linear
import numpy as np
import plotly.express as px
from shared import access, diffs
from shiny.express import input, render, ui
from shinyswatch import theme
from shinywidgets import render_widget

tiles_provider = "CartoDB PositronNoLabels"

ui.page_opts(title="Access using ML", fillable=True)
theme.darkly()


# with ui.sidebar():
#     ui.input_select("var", "Select variable", choices=["total_bill", "tip"])

with ui.nav_panel("Speed Differences"):
    ui.h1("Differences Between Speed Limits and Machine Learning Predicted Travel Speeds")
    
    # todo: add more information here
    
    @render.ui
    def map_diffs():
        return diffs.explore(column="diff_mph", legend=True, cmap="RdBu", vmax=15, vmin=-15,  tiles=tiles_provider)

with ui.nav_panel("Speed Diff Hist"):
    @render_widget
    def hist():
        return px.histogram(diffs, "diff_mph")
    
with ui.nav_panel("Difference in Access"):
    ui.input_selectize(
        "access_col",
        "Choose an access measure:",
        {
            'diff_fca_30_BEDS': "FCA 30",
            'diff_fca_60_BEDS': "FCA 60",
            'diff_2sfca_30_BEDS': "2SFCA 30",
            'diff_2sfca_60_BEDS': "2SFCA 60",
            'diff_e2sfca_30_BEDS': "E2SFCA 30",
            'diff_e2sfca_60_BEDS': "E2SFCA 60",
            'diff_g2sfca10_BEDS': "G2SFCA 30",
            'diff_g2sfca20_BEDS': "G2SFCA 60",
            'diff_3sfca_BEDS': "3SFCA",
            'diff_raam30_BEDS': "RAAM 30",
            'diff_raam60_BEDS': "RAAM 60"
        }
    )
    @render.ui
    def map_diff_access():
        vmin = np.percentile(access[access[input.access_col()] < 0][input.access_col()], 10)
        vmax = np.percentile(access[access[input.access_col()] > 0][input.access_col()], 90)
        print(vmin, vmax)
        limit = max(-vmin, vmax)
        print(limit)
        vmin, vmax = -limit, limit
        return access.explore(column=input.access_col(), legend=True, cmap="RdBu", tiles=tiles_provider,  tooltip=['GEOID', input.access_col()], vmin=vmin, vmax=vmax)


with ui.nav_panel("% Difference in Access"):
    ui.input_selectize(
        "access_col_perc",
        "Choose an access measure:",
        {
            'pdiff_fca_30_BEDS': "FCA 30",
            'pdiff_fca_60_BEDS': "FCA 60",
            'pdiff_2sfca_30_BEDS': "2SFCA 30",
            'pdiff_2sfca_60_BEDS': "2SFCA 60",
            'pdiff_e2sfca_30_BEDS': "E2SFCA 30",
            'pdiff_e2sfca_60_BEDS': "E2SFCA 60",
            'pdiff_g2sfca10_BEDS': "G2SFCA 30",
            'pdiff_g2sfca20_BEDS': "G2SFCA 60",
            'pdiff_3sfca_BEDS': "3SFCA",
            'pdiff_raam30_BEDS': "RAAM 30",
            'pdiff_raam60_BEDS': "RAAM 60"
        }
    )
    @render.ui
    def map_pdiff_access():
        return access.explore(column=input.access_col_perc(), legend=True, cmap="RdBu", tiles=tiles_provider, tooltip=['GEOID', input.access_col_perc()], vmin=-15, vmax=15)
