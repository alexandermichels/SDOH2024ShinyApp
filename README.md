# SDOH 2024 Shiny App

Dashboard for the SDOH 2024 Fellowship. WIP

A journal article explaining the machine learning approach and analysis is forthcoming.


Basic layout:

* [pregen_maps.py](pregen_maps.py) creates all of the maps using Geopandas explore, saving them as html. The app only needs to serve those generated HTMLs. The histogram is still generated live using the actual data though.


To export the app, use:

```
shinylive export src_shiny_app docs
```

You can view it locally using:

```
python -m http.server --directory docs --bind localhost 8008
```

**NOTE:** You seem to have to copy the www folder to the app deployment folder.