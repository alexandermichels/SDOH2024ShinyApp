# SDOH 2024 Shiny App

Dashboard for the SDOH 2024 Fellowship. WIP

A journal article explaining the machine learning approach and analysis is forthcoming.


Basic layout:

* [pregen_maps.py](pregen_maps.py) creates all of the maps using Geopandas explore, saving them as html. The app only needs to serve those generated HTMLs. The histogram is still generated live using the actual data though.