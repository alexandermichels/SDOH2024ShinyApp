from shiny.express import app_opts, input, render, ui
from pathlib import Path

app_dir = Path(__file__).parent

# just theming and titles
ui.page_opts(title="Access using ML", fillable=True)

# required to get it to serve static files
app_opts(static_assets={"/www": str(app_dir / 'www')})


with ui.nav_panel("About"):
    ui.h1("About")
    ui.markdown("This work examines how speed limits vary from the actual travel speeds on urban roads, affecting spatial accessiblity measures. We use machine learning trained on granular travel-time data to dervive our predicted travel speeds and then compare a variety of spatial accessibility measures using speed limits and our predicted travel speeds.")
    ui.markdown("""
                The spatial accessiblity measures used throughout are access to hospital beds in Cincinatti, OH. They are calculated using the [PySAL access package](https://pysal.org/access/) ([see their paper here](https://doi.org/10.1007/s42001-021-00126-8)). The measures considered are:
                * [Floating Catchment Area (FCA)](https://doi.org/10.1111/0033-0124.00210), using a 60 minute threshold.
                * [Two-Step Floating Catchment Area (2SFCA)](https://doi.org/10.1068/b29120), using a 60 minute threshold.
                * [Enhanced Two-Step Floating Catchment Area (E2SFCA)](https://doi.org/10.1016/j.healthplace.2009.06.002), using a 60 minute threshold.
                * [Gaussian Two-Step Floating Catchment Area (G2SFCA)](https://doi.org/10.1080/00045608.2012.657146), using sigma (&sigma;) of 20.
                * [Three-Step Floating Catchment Area (3SFCA)](https://doi.org/10.1080/13658816.2011.624987)
                * [Rational Agent Access Model (RAAM)](https://doi.org/10.1080/24694452.2019.1629870), using tau (&tau;) of 60.
                
                A journal article on this work is forthcoming.
                """)
    
    ui.h3("Author")
    ui.markdown("This research and dashboard are the work of [Alexander Michels](https://alexandermichels.github.io/), a PhD candidate at the University of Illinois Urbana-Champaign.")
    ui.h3("Funding")
    ui.markdown("This dashboard is funded by the [The SDOH & Place Project](https://sdohplace.org/) through the [SDOH & Place Fellowship Program](https://sdohplace.org/fellows). This research is funded by [The SDOH & Place Project](https://sdohplace.org/), the [CyberGIS Center](https://cybergis.illinois.edu/), and [I-GUIDE](https://i-guide.io/).")


# speed differences page
with ui.nav_panel("Speed Differences"):
    ui.h1("Differences Between Speed Limits and Average Travel Speeds")
    ui.markdown("The map and histograms below demonstrate the difference between OSM speed limits (with [osmnx](https://osmnx.readthedocs.io/en/stable/user-reference.html#osmnx.routing.add_edge_speeds) used to impute missing data) on road segments and the average travel speeds on each road segment. These actual travel speeds were used to train an ML model to predict travel speeds for all road segments in Cincinatti.")
    @render.ui
    def map_diffs():
        return ui.tags.iframe(src=f"/www/SpeedDiff.html", width="100%", height="75%")

    # @render_widget
    # def hist():
    #     return px.histogram(diffs, "diff_mph")
    
# with ui.nav_panel("Difference in Access"):
#     ui.markdown("Differences in access are calculated as the access measuring using OSM minus the access measured using ML predicted travel times. Thus, positive values are areas where OSM over-estimated access relative to ML predicted and negative values are locations where OSM under-estimated access relative to OSM. For an explanation of the various measures, see the About page.")
#     ui.input_selectize(
#         "access_col",
#         "Choose an access measure:",
#         {
#             # 'diff_fca_30_BEDS': "FCA 30",
#             'diff_fca_60_BEDS': "FCA 60",
#             # 'diff_2sfca_30_BEDS': "2SFCA 30",
#             'diff_2sfca_60_BEDS': "2SFCA 60",
#             # 'diff_e2sfca_30_BEDS': "E2SFCA 30",
#             'diff_e2sfca_60_BEDS': "E2SFCA 60",
#             # 'diff_g2sfca10_BEDS': "G2SFCA 10",
#             'diff_g2sfca20_BEDS': "G2SFCA 20",
#             'diff_3sfca_BEDS': "3SFCA",
#             # 'diff_raam30_BEDS': "RAAM 30",
#             'diff_raam60_BEDS': "RAAM 60"
#         }
#     )
#     @render.ui
#     def map_diff_access():
#         return ui.tags.iframe(src=f"/www/Diff-{input.access_col()}.html", width="100%", height="75%")


with ui.nav_panel("% Difference in Access"):
    ui.markdown("""Percentage differences in access are calculated as the access measuring using OSM minus the access measured using ML predicted travel times, then dividing by the average value between the two approaches, and finally multiplying by 100.
    Thus, positive values are areas where OSM over-estimated access relative to ML predicted and negative values are locations where OSM under-estimated access relative to OSM.
    For an explanation of the various measures, see the About page.""")
    ui.input_selectize(
        "access_col_perc",
        "Choose an access measure:",
        {
            # 'pdiff_fca_30_BEDS': "FCA 30",
            'pdiff_fca_60_BEDS': "FCA 60",
            # 'pdiff_2sfca_30_BEDS': "2SFCA 30",
            'pdiff_2sfca_60_BEDS': "2SFCA 60",
            # 'pdiff_e2sfca_30_BEDS': "E2SFCA 30",
            'pdiff_e2sfca_60_BEDS': "E2SFCA 60",
            # 'pdiff_g2sfca10_BEDS': "G2SFCA 10",
            'pdiff_g2sfca20_BEDS': "G2SFCA 20",
            'pdiff_3sfca_BEDS': "3SFCA",
            # 'pdiff_raam30_BEDS': "RAAM 30",
            'pdiff_raam60_BEDS': "RAAM 60"
        }
    )
    @render.ui
    def map_pdiff_access():
        return ui.tags.iframe(src=f"/www/Perc-{input.access_col_perc()}.html", width="100%", height="75%")
