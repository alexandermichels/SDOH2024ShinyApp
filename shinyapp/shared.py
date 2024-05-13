import geopandas as gpd
from pathlib import Path

app_dir = Path(__file__).parent
diffs = gpd.read_feather(app_dir / "data/Diffs.feather")
