import folium
import geopandas as gpd
import numpy as np
from pathlib import Path


tiles_provider = "CartoDB PositronNoLabels"

app_dir = Path(__file__).parent
access = gpd.read_file(app_dir / "data/AccessibilityDiffSimplified.gpkg")

# make the directory to store stuff
html_dir = Path(__file__).parent / "shinyapp/www"
html_dir.mkdir(exist_ok=True)


diffs = gpd.read_feather(app_dir / "data/Diffs.feather")
diffs["diff_mph"] = diffs["diff_mph"].round(2)
m = diffs.explore(column="diff_mph", legend=True, cmap="RdBu", vmax=15, vmin=-15,  tiles=tiles_provider)
m.save(html_dir / "SpeedDiff.html")


# measure_dict = {
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

# for k, v in measure_dict.items():
#     tmp = access[["GEOID", k, "geometry"]]
#     tmp[v] = tmp[k]
#     tmp = tmp.drop(columns=[k])
#     print(tmp.columns)
#     limit = np.percentile(np.abs(tmp[tmp[v] > 0][v]), 90)
#     print(limit)
#     vmin, vmax = -limit, limit
#     m = tmp.explore(column=v, legend=True, cmap="RdBu", tiles=tiles_provider,  tooltip=['GEOID', v], vmin=vmin, vmax=vmax)
#     m.save(html_dir / f"Diff-{k}.html")
    
pmeasure_dict = {
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

for k, v in pmeasure_dict.items():
    tmp = access[["GEOID", k, "geometry"]]
    tmp[v] = tmp[k].round(2)
    tmp = tmp.drop(columns=[k])
    m = tmp.explore(column=v, legend=True, cmap="RdBu", tiles=tiles_provider,  tooltip=['GEOID', v], vmin=-15, vmax=15)
    m.save(html_dir / f"Perc-{k}.html")