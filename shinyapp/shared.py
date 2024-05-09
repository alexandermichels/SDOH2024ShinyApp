import geopandas as gpd
from ipyleaflet import GeoData
from pathlib import Path

app_dir = Path(__file__).parent
diffs = gpd.read_feather(app_dir / "data/Diffs.feather")
access = gpd.read_file(app_dir / "data/AccessibilityDiff.gpkg")