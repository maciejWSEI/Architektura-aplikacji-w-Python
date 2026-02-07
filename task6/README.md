## Data processing

The program reads meteorological data from the IMGW XML API.

For each station, it extracts:

- station name (`nazwa_stacji`)
- average wind speed (`wiatr_srednia_predkosc`)

The data is filtered and converted to numeric values, then visualized
as a bar chart showing wind speed for selected stations.

Correct XML tag names are required; otherwise no data will be displayed.
